from enum import Enum


class RecordRecordIDCreate():
    def __init__(self, uuid, recordStatus, created, updated, deleted,
                 recordData):
        self.recordId = uuid
        self.info = RecordInfoCreate(recordStatus, created, updated, deleted,
                                     recordData)


class RecordInfoCreate():
    def __init__(self, recordStatus, created, updated, deleted, recordData):
        self.recordStatus = recordStatus
        self.created = created
        self.updated = updated
        self.deleted = deleted
        self.recordData = recordData


class StatusRecord(Enum):
    NEW = "NEW"
    UPDATED = "UPDATED"
    DELETED = "DELETED"
