FROM python:3

ADD lifx_with_sonos.py /
ADD images /
RUN pip install pylifxtiles
RUN pip install soco

CMD [ "python", "./lifx_with_sonos.py" ]