.PHONY:all

sensitivity.h5: spec.h5
	python3 NdSensitivity.py --discri 0 0.5 1 -o $@ -i $^