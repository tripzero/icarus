#ifndef MPPT_H_
#define MPPT_H_

#include <Adafruit_INA219.h>

class Mppt
{
public:
	typedef float (*InputVoltsToOutputVolts)(float);
	enum Mode {
		Sweeping = 0,
		Searching,
		Manual,

		SweepUp,
		SweepDown
	};

	enum Condition {
		ConditionNotSet = 1,
		PowerDrop = 1 << 1,
		PowerIncrease = 1 << 2,
		PowerOrVoltsExceededMax = 1 << 3,
		InputVoltsDroppedBelowThreshold = 1 << 4
	};

	Mppt(int mosfetPin, Adafruit_INA219 *output, int inputVoltPin = -1);

	void begin(Mode mode, int targetVolts, uint16_t _delay);

	void poll();

	void setMode(Mode mode)
	{
		pwmMode = mode;
	}

	int condition()
	{
		return mCondition;
	}

	void setPwmValue(int v)
	{
		if(v < 0 || v > 255)
			return;

		pwmMode = Manual;
		pwmValue = v;
	}

	void setInputThreshold(int v)
	{
		inputThresholdVolts = v;
	}

	int getPwmValue()
	{
		return pwmValue;
	}

	int getHighWatts()
	{
		return highWatts;
	}

	float getSystemVolts()
	{
		return inputVolts;
	}

	int getOutputVolts()
	{
		return outputVolts;
	}

	int getOutputCurrent()
	{
		return outputCurrent;
	}

	int getOutputPower()
	{
		return outputWatts;
	}

	Mode getMode() { return pwmMode; }

	void setOutputToInputFunctor(InputVoltsToOutputVolts i)
	{
		oToI = i;
	}

private:
	Adafruit_INA219 * output;
	int inputVoltPin;
	Mode pwmMode;
	int pwmValue;
	int pwmInc;
	int targetVolts;
	int outputVolts;
	int outputCurrent;
	const int mosfet;
	uint32_t tick;
	int highWatts;
	int prevWatts;
	float outputWatts;
	int maxWatts;
	Mode sweepMode;
	InputVoltsToOutputVolts oToI;
	float inputVolts;
	int inputThresholdVolts;
	uint32_t mCondition;
	uint16_t mDelay;
	uint16_t timer;
	int wattSamples[5];
	int numSamples;
};

#endif
