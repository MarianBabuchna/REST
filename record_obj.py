from enum import Enum

class record_recordID_create():
    def __init__(self,uuid,recordStatus,created,updated,deleted,recordData):
        self.recordId = uuid
        self.info = record_info_create(recordStatus,created,updated,deleted,recordData)

class record_info_create():
    def __init__(self,recordStatus,created,updated,deleted,recordData):
        self.recordStatus=recordStatus
        self.created=created
        self.updated=updated
        self.deleted=deleted
        self.recordData=recordData

class status_record(Enum):
    NEW="NEW"
    UPDATED="UPDATED"
    DELETED="DELETED"
