#include "Mppt.h"

Mppt::Mppt(int mosfetPin, Adafruit_INA219 *o, int i)
	:mosfet(mosfetPin), output(o), inputVoltPin(i), pwmMode(Searching), pwmValue(0),
	  tick(0), highWatts(0), prevWatts(0), maxWatts(10), pwmInc(1), targetVolts(0),
	  sweepMode(SweepUp), inputVolts(-1), mDelay(1), outputCurrent(0), outputVolts(0),
	  outputWatts(0), inputThresholdVolts(0), mCondition(ConditionNotSet), timer(500),
	  numSamples(0)
{
	oToI = [](float o) -> float
	{
		//Vin = Vout / (R2 / (R1 + R2))
		return o / (194.0 / (1000.0 + 194.0));
	};
}

void Mppt::begin(Mppt::Mode mode, int targetVolts, uint16_t _delay)
{
	mDelay = _delay;
	pwmMode = mode;
	Mppt::targetVolts = targetVolts;
	output->begin();
}

void Mppt::poll()
{
	tick++;

	if((mDelay && tick < timer / mDelay) || tick < timer)
	{
		return;
	}

	tick = 0;

	int tempCurrent = output->getCurrent_mA();
	int tempVolts = output->getBusVoltage_V();

	if(tempCurrent)
	{
		outputCurrent = tempCurrent;
	}
	if(tempVolts && tempCurrent)
		outputVolts = tempVolts;

	int tempWatt = (float)outputVolts * ((float)outputCurrent / 1000.0);

	wattSamples[numSamples++] = tempWatt;

	if(numSamples == 5)
	{
		outputWatts = (double)(wattSamples[0] + wattSamples[1] + wattSamples[2] + wattSamples[3] + wattSamples[4]) / 5.0;
		numSamples=0;
	}

	if(inputVoltPin >= 0)
	{
		inputVolts = analogRead(inputVoltPin) * (3.3 / 1023.0);

		inputVolts = oToI(inputVolts);
	}

	if (outputWatts > highWatts)
	{
		highWatts = outputWatts;
	}

	if(pwmMode == Searching)
	{
		mCondition = ConditionNotSet;

		if (outputWatts > 0 && outputWatts < prevWatts)
		{
			mCondition = PowerDrop;
			pwmInc = -1;
		}
		else
		{
			mCondition = PowerIncrease;
			pwmInc = 1;
		}

		prevWatts = outputWatts;

		if(outputVolts > targetVolts || outputWatts > maxWatts)
		{
			mCondition |= (Condition)PowerOrVoltsExceededMax;
			pwmInc = -1;
		}

		if(inputVolts < inputThresholdVolts)
		{
			mCondition |= (Condition)InputVoltsDroppedBelowThreshold;
			pwmInc = -1;
		}

		pwmValue += pwmInc;
	}
	else if(pwmMode == Sweeping)
	{
		if (pwmValue >= 255)
			sweepMode = Mppt::SweepDown;
		else if (pwmValue <= 0.0)
			sweepMode = Mppt::SweepUp;

		if(sweepMode == Mppt::SweepUp)
			pwmInc = 1;
		else pwmInc = -1;

		pwmValue += pwmInc;
	}

	if (pwmValue > 255) pwmValue = 255;
	if (pwmValue < 0) pwmValue = 0;

	analogWrite(mosfet, pwmValue);
}
