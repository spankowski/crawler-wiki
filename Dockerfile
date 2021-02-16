# set base image (host OS)
FROM scrapinghub/scrapyrt

# install dependencies
RUN pip install Pillow
