RUN=uvicorn app.main:app --reload

.PHONY: run

run:
	$(RUN)
