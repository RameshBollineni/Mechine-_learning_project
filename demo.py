import logging
from sklearn import pipeline
from housing.pipeline.pipeline import Pipeline

def main( ):
    try:
        pipeline=pipeline()
        pipeline.run_pipeline()
    except Exception as e:
        logging.error(f"{e}")
        print(e)


if __name__ == "__main__":
      main()

