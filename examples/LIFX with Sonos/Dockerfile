FROM python:3

ADD lifx_with_sonos.py /
RUN pip install pylifxtiles==0.1.8
RUN pip install soco

CMD [ "python", "./lifx_with_sonos.py" ]