FROM public.ecr.aws/lambda/python:3.10
COPY requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
COPY app.py ${LAMBDA_TASK_ROOT}
# Make sure to change this to your api key
ENV API_KEY "ADD_API_KEY_HERE"
CMD [ "app.handler" ]