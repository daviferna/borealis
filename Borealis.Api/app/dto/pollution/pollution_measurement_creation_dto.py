class PollutionMeasurementCreationDto():
    def __init__(self, id, datetime, magnitude_id, station_id, data, validation_code):
        self.datetime = datetime
        self.magnitude_id = magnitude_id
        self.station_id = station_id
        self.data = data
        self.validation_code = validation_code


