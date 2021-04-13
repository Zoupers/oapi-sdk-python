# -*- coding: UTF-8 -*-
# Code generated by lark suite oapi sdk gen

from typing import List, Dict, Any
from ....event.model.event import *
import attr




@attr.s
class ReservePermissionChecker(object):
    check_field = attr.ib(type=int, default=None, metadata={'json': 'check_field'})
    check_mode = attr.ib(type=int, default=None, metadata={'json': 'check_mode'})
    check_list = attr.ib(type=List[str], default=None, metadata={'json': 'check_list'})


@attr.s
class ReserveActionPermission(object):
    permission = attr.ib(type=int, default=None, metadata={'json': 'permission'})
    permission_checkers = attr.ib(type=List[ReservePermissionChecker], default=None, metadata={'json': 'permission_checkers'})


@attr.s
class ReserveMeetingSetting(object):
    topic = attr.ib(type=str, default=None, metadata={'json': 'topic'})
    action_permissions = attr.ib(type=List[ReserveActionPermission], default=None, metadata={'json': 'action_permissions'})


@attr.s
class Reserve(object):
    __int_to_string_fields__ = attr.ib(type=List[str], default=["id", "end_time"])
    id = attr.ib(type=int, default=None, metadata={'json': 'id'})
    meeting_no = attr.ib(type=str, default=None, metadata={'json': 'meeting_no'})
    url = attr.ib(type=str, default=None, metadata={'json': 'url'})
    app_link = attr.ib(type=str, default=None, metadata={'json': 'app_link'})
    end_time = attr.ib(type=int, default=None, metadata={'json': 'end_time'})
    expire_status = attr.ib(type=int, default=None, metadata={'json': 'expire_status'})
    reserve_user_id = attr.ib(type=str, default=None, metadata={'json': 'reserve_user_id'})
    meeting_settings = attr.ib(type=ReserveMeetingSetting, default=None, metadata={'json': 'meeting_settings'})


@attr.s
class ReportMeetingDaily(object):
    __int_to_string_fields__ = attr.ib(type=List[str], default=["date", "meeting_count", "meeting_duration", "participant_count"])
    date = attr.ib(type=int, default=None, metadata={'json': 'date'})
    meeting_count = attr.ib(type=int, default=None, metadata={'json': 'meeting_count'})
    meeting_duration = attr.ib(type=int, default=None, metadata={'json': 'meeting_duration'})
    participant_count = attr.ib(type=int, default=None, metadata={'json': 'participant_count'})


@attr.s
class Report(object):
    __int_to_string_fields__ = attr.ib(type=List[str], default=["total_meeting_count", "total_meeting_duration", "total_participant_count"])
    total_meeting_count = attr.ib(type=int, default=None, metadata={'json': 'total_meeting_count'})
    total_meeting_duration = attr.ib(type=int, default=None, metadata={'json': 'total_meeting_duration'})
    total_participant_count = attr.ib(type=int, default=None, metadata={'json': 'total_participant_count'})
    daily_report = attr.ib(type=List[ReportMeetingDaily], default=None, metadata={'json': 'daily_report'})


@attr.s
class RoomDigitalSignageMaterial(object):
    id = attr.ib(type=str, default=None, metadata={'json': 'id'})
    name = attr.ib(type=str, default=None, metadata={'json': 'name'})
    material_type = attr.ib(type=int, default=None, metadata={'json': 'material_type'})
    url = attr.ib(type=str, default=None, metadata={'json': 'url'})
    duration = attr.ib(type=int, default=None, metadata={'json': 'duration'})
    cover = attr.ib(type=str, default=None, metadata={'json': 'cover'})
    md5 = attr.ib(type=str, default=None, metadata={'json': 'md5'})


@attr.s
class RoomDigitalSignage(object):
    enable = attr.ib(type=bool, default=None, metadata={'json': 'enable'})
    mute = attr.ib(type=bool, default=None, metadata={'json': 'mute'})
    start_display = attr.ib(type=int, default=None, metadata={'json': 'start_display'})
    stop_display = attr.ib(type=int, default=None, metadata={'json': 'stop_display'})
    materials = attr.ib(type=List[RoomDigitalSignageMaterial], default=None, metadata={'json': 'materials'})


@attr.s
class RoomConfig(object):
    room_background = attr.ib(type=str, default=None, metadata={'json': 'room_background'})
    display_background = attr.ib(type=str, default=None, metadata={'json': 'display_background'})
    digital_signage = attr.ib(type=RoomDigitalSignage, default=None, metadata={'json': 'digital_signage'})


@attr.s
class MeetingUser(object):
    id = attr.ib(type=str, default=None, metadata={'json': 'id'})
    user_type = attr.ib(type=int, default=None, metadata={'json': 'user_type'})


@attr.s
class MeetingParticipant(object):
    id = attr.ib(type=str, default=None, metadata={'json': 'id'})
    user_type = attr.ib(type=int, default=None, metadata={'json': 'user_type'})
    is_host = attr.ib(type=bool, default=None, metadata={'json': 'is_host'})
    is_cohost = attr.ib(type=bool, default=None, metadata={'json': 'is_cohost'})
    is_external = attr.ib(type=bool, default=None, metadata={'json': 'is_external'})
    status = attr.ib(type=int, default=None, metadata={'json': 'status'})


@attr.s
class MeetingAbility(object):
    use_video = attr.ib(type=bool, default=None, metadata={'json': 'use_video'})
    use_audio = attr.ib(type=bool, default=None, metadata={'json': 'use_audio'})
    use_share_screen = attr.ib(type=bool, default=None, metadata={'json': 'use_share_screen'})
    use_follow_screen = attr.ib(type=bool, default=None, metadata={'json': 'use_follow_screen'})
    use_recording = attr.ib(type=bool, default=None, metadata={'json': 'use_recording'})
    use_pstn = attr.ib(type=bool, default=None, metadata={'json': 'use_pstn'})


@attr.s
class Meeting(object):
    __int_to_string_fields__ = attr.ib(type=List[str], default=["id", "create_time", "start_time", "end_time", "participant_count"])
    id = attr.ib(type=int, default=None, metadata={'json': 'id'})
    topic = attr.ib(type=str, default=None, metadata={'json': 'topic'})
    url = attr.ib(type=str, default=None, metadata={'json': 'url'})
    create_time = attr.ib(type=int, default=None, metadata={'json': 'create_time'})
    start_time = attr.ib(type=int, default=None, metadata={'json': 'start_time'})
    end_time = attr.ib(type=int, default=None, metadata={'json': 'end_time'})
    host_user = attr.ib(type=MeetingUser, default=None, metadata={'json': 'host_user'})
    status = attr.ib(type=int, default=None, metadata={'json': 'status'})
    participant_count = attr.ib(type=int, default=None, metadata={'json': 'participant_count'})
    participants = attr.ib(type=List[MeetingParticipant], default=None, metadata={'json': 'participants'})
    ability = attr.ib(type=MeetingAbility, default=None, metadata={'json': 'ability'})


@attr.s
class UserId(object):
    user_id = attr.ib(type=str, default=None, metadata={'json': 'user_id'})
    open_id = attr.ib(type=str, default=None, metadata={'json': 'open_id'})
    union_id = attr.ib(type=str, default=None, metadata={'json': 'union_id'})


@attr.s
class MeetingEventUser(object):
    id = attr.ib(type=UserId, default=None, metadata={'json': 'id'})
    user_role = attr.ib(type=int, default=None, metadata={'json': 'user_role'})
    user_type = attr.ib(type=int, default=None, metadata={'json': 'user_type'})


@attr.s
class MeetingEventMeeting(object):
    __int_to_string_fields__ = attr.ib(type=List[str], default=["id", "start_time", "end_time"])
    id = attr.ib(type=int, default=None, metadata={'json': 'id'})
    topic = attr.ib(type=str, default=None, metadata={'json': 'topic'})
    meeting_no = attr.ib(type=str, default=None, metadata={'json': 'meeting_no'})
    start_time = attr.ib(type=int, default=None, metadata={'json': 'start_time'})
    end_time = attr.ib(type=int, default=None, metadata={'json': 'end_time'})
    host_user = attr.ib(type=MeetingEventUser, default=None, metadata={'json': 'host_user'})
    owner = attr.ib(type=MeetingEventUser, default=None, metadata={'json': 'owner'})


@attr.s
class MeetingParticipantResult(object):
    id = attr.ib(type=str, default=None, metadata={'json': 'id'})
    user_type = attr.ib(type=int, default=None, metadata={'json': 'user_type'})
    result = attr.ib(type=int, default=None, metadata={'json': 'result'})


@attr.s
class RecordingPermissionObject(object):
    id = attr.ib(type=str, default=None, metadata={'json': 'id'})
    type = attr.ib(type=int, default=None, metadata={'json': 'type'})
    permission = attr.ib(type=int, default=None, metadata={'json': 'permission'})


@attr.s
class ReportTopUser(object):
    __int_to_string_fields__ = attr.ib(type=List[str], default=["id", "meeting_count", "meeting_duration"])
    id = attr.ib(type=int, default=None, metadata={'json': 'id'})
    name = attr.ib(type=str, default=None, metadata={'json': 'name'})
    user_type = attr.ib(type=int, default=None, metadata={'json': 'user_type'})
    meeting_count = attr.ib(type=int, default=None, metadata={'json': 'meeting_count'})
    meeting_duration = attr.ib(type=int, default=None, metadata={'json': 'meeting_duration'})


@attr.s
class MeetingInviteStatus(object):
    id = attr.ib(type=str, default=None, metadata={'json': 'id'})
    user_type = attr.ib(type=int, default=None, metadata={'json': 'user_type'})
    status = attr.ib(type=int, default=None, metadata={'json': 'status'})


@attr.s
class MeetingRecording(object):
    __int_to_string_fields__ = attr.ib(type=List[str], default=["id", "meeting_id", "duration"])
    id = attr.ib(type=int, default=None, metadata={'json': 'id'})
    meeting_id = attr.ib(type=int, default=None, metadata={'json': 'meeting_id'})
    url = attr.ib(type=str, default=None, metadata={'json': 'url'})
    duration = attr.ib(type=int, default=None, metadata={'json': 'duration'})





@attr.s
class MeetingInviteReqBody(object):
    invitees = attr.ib(type=List[MeetingUser], default=None, metadata={'json': 'invitees'})


@attr.s
class MeetingInviteResult(object):
    invite_results = attr.ib(type=List[MeetingInviteStatus], default=None, metadata={'json': 'invite_results'})



@attr.s
class MeetingListResult(object):
    has_more = attr.ib(type=bool, default=None, metadata={'json': 'has_more'})
    page_token = attr.ib(type=str, default=None, metadata={'json': 'page_token'})
    meetings = attr.ib(type=List[Meeting], default=None, metadata={'json': 'meetings'})



@attr.s
class ReportGetTopUserResult(object):
    top_user_report = attr.ib(type=List[ReportTopUser], default=None, metadata={'json': 'top_user_report'})


@attr.s
class MeetingSetHostReqBody(object):
    host_user = attr.ib(type=MeetingUser, default=None, metadata={'json': 'host_user'})
    old_host_user = attr.ib(type=MeetingUser, default=None, metadata={'json': 'old_host_user'})


@attr.s
class MeetingSetHostResult(object):
    host_user = attr.ib(type=MeetingUser, default=None, metadata={'json': 'host_user'})



@attr.s
class MeetingRecordingGetResult(object):
    recording = attr.ib(type=MeetingRecording, default=None, metadata={'json': 'recording'})







@attr.s
class ReportGetDailyResult(object):
    meeting_report = attr.ib(type=Report, default=None, metadata={'json': 'meeting_report'})



@attr.s
class MeetingGetResult(object):
    meeting = attr.ib(type=Meeting, default=None, metadata={'json': 'meeting'})


@attr.s
class RoomConfigSetReqBody(object):
    __int_to_string_fields__ = attr.ib(type=List[str], default=["country_id", "district_id", "building_id", "room_id"])
    scope = attr.ib(type=int, default=None, metadata={'json': 'scope'})
    country_id = attr.ib(type=int, default=None, metadata={'json': 'country_id'})
    district_id = attr.ib(type=int, default=None, metadata={'json': 'district_id'})
    building_id = attr.ib(type=int, default=None, metadata={'json': 'building_id'})
    floor_name = attr.ib(type=str, default=None, metadata={'json': 'floor_name'})
    room_id = attr.ib(type=int, default=None, metadata={'json': 'room_id'})
    room_config = attr.ib(type=RoomConfig, default=None, metadata={'json': 'room_config'})



@attr.s
class MeetingRecordingSetPermissionReqBody(object):
    permission_objects = attr.ib(type=List[RecordingPermissionObject], default=None, metadata={'json': 'permission_objects'})



@attr.s
class MeetingRecordingStartReqBody(object):
    timezone = attr.ib(type=int, default=None, metadata={'json': 'timezone'})



@attr.s
class ReserveUpdateReqBody(object):
    __int_to_string_fields__ = attr.ib(type=List[str], default=["end_time"])
    end_time = attr.ib(type=int, default=None, metadata={'json': 'end_time'})
    meeting_settings = attr.ib(type=ReserveMeetingSetting, default=None, metadata={'json': 'meeting_settings'})


@attr.s
class ReserveUpdateResult(object):
    reserve = attr.ib(type=Reserve, default=None, metadata={'json': 'reserve'})


@attr.s
class ReserveApplyReqBody(object):
    __int_to_string_fields__ = attr.ib(type=List[str], default=["end_time"])
    end_time = attr.ib(type=int, default=None, metadata={'json': 'end_time'})
    meeting_settings = attr.ib(type=ReserveMeetingSetting, default=None, metadata={'json': 'meeting_settings'})


@attr.s
class ReserveApplyResult(object):
    reserve = attr.ib(type=Reserve, default=None, metadata={'json': 'reserve'})



@attr.s
class ReserveGetResult(object):
    reserve = attr.ib(type=Reserve, default=None, metadata={'json': 'reserve'})



@attr.s
class ReserveGetActiveMeetingResult(object):
    meeting = attr.ib(type=Meeting, default=None, metadata={'json': 'meeting'})




@attr.s
class MeetingLeaveMeetingEventData(object):
    meeting = attr.ib(type=MeetingEventMeeting, default=None, metadata={'json': 'meeting'})
    operator = attr.ib(type=MeetingEventUser, default=None, metadata={'json': 'operator'})
    leave_reason = attr.ib(type=int, default=None, metadata={'json': 'leave_reason'})


@attr.s
class MeetingLeaveMeetingEvent(BaseEventV2):
    event = attr.ib(type=MeetingLeaveMeetingEventData, default=None)



@attr.s
class MeetingMeetingEndedEventData(object):
    meeting = attr.ib(type=MeetingEventMeeting, default=None, metadata={'json': 'meeting'})
    operator = attr.ib(type=MeetingEventUser, default=None, metadata={'json': 'operator'})


@attr.s
class MeetingMeetingEndedEvent(BaseEventV2):
    event = attr.ib(type=MeetingMeetingEndedEventData, default=None)



@attr.s
class MeetingMeetingStartedEventData(object):
    meeting = attr.ib(type=MeetingEventMeeting, default=None, metadata={'json': 'meeting'})
    operator = attr.ib(type=MeetingEventUser, default=None, metadata={'json': 'operator'})


@attr.s
class MeetingMeetingStartedEvent(BaseEventV2):
    event = attr.ib(type=MeetingMeetingStartedEventData, default=None)



@attr.s
class MeetingRecordingEndedEventData(object):
    meeting = attr.ib(type=MeetingEventMeeting, default=None, metadata={'json': 'meeting'})
    operator = attr.ib(type=MeetingEventUser, default=None, metadata={'json': 'operator'})


@attr.s
class MeetingRecordingEndedEvent(BaseEventV2):
    event = attr.ib(type=MeetingRecordingEndedEventData, default=None)



@attr.s
class MeetingShareEndedEventData(object):
    meeting = attr.ib(type=MeetingEventMeeting, default=None, metadata={'json': 'meeting'})
    operator = attr.ib(type=MeetingEventUser, default=None, metadata={'json': 'operator'})


@attr.s
class MeetingShareEndedEvent(BaseEventV2):
    event = attr.ib(type=MeetingShareEndedEventData, default=None)



@attr.s
class MeetingJoinMeetingEventData(object):
    meeting = attr.ib(type=MeetingEventMeeting, default=None, metadata={'json': 'meeting'})
    operator = attr.ib(type=MeetingEventUser, default=None, metadata={'json': 'operator'})


@attr.s
class MeetingJoinMeetingEvent(BaseEventV2):
    event = attr.ib(type=MeetingJoinMeetingEventData, default=None)



@attr.s
class MeetingRecordingStartedEventData(object):
    meeting = attr.ib(type=MeetingEventMeeting, default=None, metadata={'json': 'meeting'})
    operator = attr.ib(type=MeetingEventUser, default=None, metadata={'json': 'operator'})


@attr.s
class MeetingRecordingStartedEvent(BaseEventV2):
    event = attr.ib(type=MeetingRecordingStartedEventData, default=None)



@attr.s
class MeetingSendMeetingImEventData(object):
    meeting = attr.ib(type=MeetingEventMeeting, default=None, metadata={'json': 'meeting'})
    operator = attr.ib(type=MeetingEventUser, default=None, metadata={'json': 'operator'})
    content = attr.ib(type=str, default=None, metadata={'json': 'content'})


@attr.s
class MeetingSendMeetingImEvent(BaseEventV2):
    event = attr.ib(type=MeetingSendMeetingImEventData, default=None)



@attr.s
class MeetingShareStartedEventData(object):
    meeting = attr.ib(type=MeetingEventMeeting, default=None, metadata={'json': 'meeting'})
    operator = attr.ib(type=MeetingEventUser, default=None, metadata={'json': 'operator'})


@attr.s
class MeetingShareStartedEvent(BaseEventV2):
    event = attr.ib(type=MeetingShareStartedEventData, default=None)



@attr.s
class MeetingRecordingReadyEventData(object):
    meeting = attr.ib(type=MeetingEventMeeting, default=None, metadata={'json': 'meeting'})
    url = attr.ib(type=str, default=None, metadata={'json': 'url'})
    duration = attr.ib(type=int, default=None, metadata={'json': 'duration'})


@attr.s
class MeetingRecordingReadyEvent(BaseEventV2):
    event = attr.ib(type=MeetingRecordingReadyEventData, default=None)
