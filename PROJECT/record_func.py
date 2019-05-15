from PROJECT import record_obj
import json
import uuid
from datetime import datetime, timezone
from collections import namedtuple


##########################################
# CONSTANTS
##########################################
OUTPUT_FILE_JSON = "stored_records.json"


def uuid4_generate():
    uuid4 = uuid.uuid4()
    return str(uuid4)


def date_time_generate():
    local_time = datetime.now(timezone.utc).astimezone()
    date_time = local_time.isoformat()
    return str(date_time)


def record_write_new_json(uuid):
    if uuid == "":
        uuid = uuid4_generate()
    recordStatus = record_obj.StatusRecord.NEW.value
    created = date_time_generate()
    record = record_obj.RecordRecordIDCreate(uuid, recordStatus,
                                             created, "", "", "")
    json_string = json.dumps(record.__dict__, default=obj_to_dict)
    json_string_serial = json.loads(json_string)
    file_record_append(json_string_serial)



def obj_to_dict(obj):
    return obj.__dict__


def file_read_json():
    json_file = open(OUTPUT_FILE_JSON, "r")
    records_list = json_file.readlines()
    json_file.close()
    return records_list


def json_record_deserialize(record):
    x = json.loads(record, object_hook=lambda d:
                   namedtuple('X', d.keys())(*d.values()))
    record = record_obj.RecordRecordIDCreate(x.recordId, x.info.recordStatus,
                                             x.info.created, x.info.updated,
                                             x.info.deleted, x.info.recordData)
    return record


def record_uuid_get(uuid):
    records_list = file_read_json()
    for i in range(len(records_list)):
        record_line = records_list[i].replace("\n", "")
        record_obj = json_record_deserialize(str(record_line))
        if record_obj.recordId == uuid:
            return record_line
    response = "Record with " + uuid + " NOT found !!!"
    return response


def record_uuid_delete(uuid):
    records_list = file_read_json()
    for i in range(len(records_list)):
        record_line = records_list[i].replace("\n", "")
        record = json_record_deserialize(str(record_line))
        if record.recordId == uuid:
            found_record_index = i
            record.info.recordStatus = record_obj.StatusRecord.DELETED.value
            record.info.deleted = date_time_generate()
            del(records_list[found_record_index])
            file_records_write(records_list)

            json_string = json.dumps(record.__dict__, default=obj_to_dict)
            json_string_serial = json.loads(json_string)
            file_record_append(json_string_serial)
            break
    response = "Record with " + uuid + " NOT found !!!"
    return response


def record_uuid_patch(uuid):
    records_list = file_read_json()
    for i in range(len(records_list)):
        record_line = records_list[i].replace("\n", "")
        record = json_record_deserialize(str(record_line))
        if record.recordId == uuid:
            # JsonPatch
            found_record_index = i
            record.info.recordStatus = record_obj.StatusRecord.UPDATED.value

            if (record.info.updated == ""):
                record.info.updated = date_time_generate()
            else:
                record.info.updated = record.info.updated + "," \
                                    + date_time_generate()

            del (records_list[found_record_index])
            file_records_write(records_list)

            json_string = json.dumps(record.__dict__, default=obj_to_dict)
            json_string_serial = json.loads(json_string)
            file_record_append(json_string_serial)
            break


def file_record_append(json_string_serial):
    try:
        with open(OUTPUT_FILE_JSON, 'a') as f:
            json.dump(json_string_serial, f)
            f.write('\n')
    except IOError:
        print ("!!! Problem to open file:", OUTPUT_FILE_JSON)
    else:
            f.close()


def file_records_write(records_list):
    try:
        with open(OUTPUT_FILE_JSON, 'w') as f:
            f.writelines(records_list)
    except IOError:
            print("!!! Problem to open file:", OUTPUT_FILE_JSON)
    else:
            f.close()
