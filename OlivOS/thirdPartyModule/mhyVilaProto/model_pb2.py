# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: model.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bmodel.proto\x12\x08vila_bot\"\xf8\x02\n\rRobotTemplate\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x03 \x01(\t\x12\x0c\n\x04icon\x18\x04 \x01(\t\x12\x31\n\x08\x63ommands\x18\x05 \x03(\x0b\x32\x1f.vila_bot.RobotTemplate.Command\x12>\n\x0f\x63ustom_settings\x18\x06 \x03(\x0b\x32%.vila_bot.RobotTemplate.CustomSetting\x12%\n\x1dis_allowed_add_to_other_villa\x18\x07 \x01(\x08\x1a\x15\n\x05Param\x12\x0c\n\x04\x64\x65sc\x18\x01 \x01(\t\x1aT\n\x07\x43ommand\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\t\x12-\n\x06params\x18\x03 \x03(\x0b\x32\x1d.vila_bot.RobotTemplate.Param\x1a*\n\rCustomSetting\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\"D\n\x05Robot\x12)\n\x08template\x18\x01 \x01(\x0b\x32\x17.vila_bot.RobotTemplate\x12\x10\n\x08villa_id\x18\x02 \x01(\x04\"\xb7\x01\n\x10QuoteMessageInfo\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\x12\x0f\n\x07msg_uid\x18\x02 \x01(\t\x12\x0f\n\x07send_at\x18\x03 \x01(\x03\x12\x10\n\x08msg_type\x18\x04 \x01(\t\x12\x12\n\nbot_msg_id\x18\x05 \x01(\t\x12\x14\n\x0c\x66rom_user_id\x18\x06 \x01(\x04\x12\x18\n\x10\x66rom_user_id_str\x18\x07 \x01(\t\x12\x1a\n\x12\x66rom_user_nickname\x18\x08 \x01(\t\"\xbd\x0f\n\nRobotEvent\x12\x1e\n\x05robot\x18\x01 \x01(\x0b\x32\x0f.vila_bot.Robot\x12,\n\x04type\x18\x02 \x01(\x0e\x32\x1e.vila_bot.RobotEvent.EventType\x12\x34\n\x0b\x65xtend_data\x18\x03 \x01(\x0b\x32\x1f.vila_bot.RobotEvent.ExtendData\x12\x12\n\ncreated_at\x18\x04 \x01(\x03\x12\n\n\x02id\x18\x05 \x01(\t\x12\x0f\n\x07send_at\x18\x06 \x01(\x03\x1a\xcf\x0c\n\nExtendData\x12\x43\n\njoin_villa\x18\x01 \x01(\x0b\x32-.vila_bot.RobotEvent.ExtendData.JoinVillaInfoH\x00\x12G\n\x0csend_message\x18\x02 \x01(\x0b\x32/.vila_bot.RobotEvent.ExtendData.SendMessageInfoH\x00\x12G\n\x0c\x63reate_robot\x18\x03 \x01(\x0b\x32/.vila_bot.RobotEvent.ExtendData.CreateRobotInfoH\x00\x12G\n\x0c\x64\x65lete_robot\x18\x04 \x01(\x0b\x32/.vila_bot.RobotEvent.ExtendData.DeleteRobotInfoH\x00\x12R\n\x12\x61\x64\x64_quick_emoticon\x18\x05 \x01(\x0b\x32\x34.vila_bot.RobotEvent.ExtendData.AddQuickEmoticonInfoH\x00\x12K\n\x0e\x61udit_callback\x18\x06 \x01(\x0b\x32\x31.vila_bot.RobotEvent.ExtendData.AuditCallbackInfoH\x00\x12T\n\x13\x63lick_msg_component\x18\x07 \x01(\x0b\x32\x35.vila_bot.RobotEvent.ExtendData.ClickMsgComponentInfoH\x00\x1a`\n\rJoinVillaInfo\x12\x10\n\x08join_uid\x18\x01 \x01(\x04\x12\x1a\n\x12join_user_nickname\x18\x02 \x01(\t\x12\x0f\n\x07join_at\x18\x03 \x01(\x03\x12\x10\n\x08villa_id\x18\x04 \x01(\x04\x1a\xfd\x01\n\x0fSendMessageInfo\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\x12\x14\n\x0c\x66rom_user_id\x18\x02 \x01(\x04\x12\x0f\n\x07send_at\x18\x03 \x01(\x03\x12)\n\x0bobject_name\x18\x04 \x01(\x0e\x32\x14.vila_bot.ObjectName\x12\x0f\n\x07room_id\x18\x05 \x01(\x04\x12\x10\n\x08nickname\x18\x06 \x01(\t\x12\x0f\n\x07msg_uid\x18\x07 \x01(\t\x12\x12\n\nbot_msg_id\x18\x08 \x01(\t\x12\x10\n\x08villa_id\x18\t \x01(\x04\x12-\n\tquote_msg\x18\n \x01(\x0b\x32\x1a.vila_bot.QuoteMessageInfo\x1a#\n\x0f\x43reateRobotInfo\x12\x10\n\x08villa_id\x18\x01 \x01(\x04\x1a#\n\x0f\x44\x65leteRobotInfo\x12\x10\n\x08villa_id\x18\x01 \x01(\x04\x1a\xbc\x01\n\x14\x41\x64\x64QuickEmoticonInfo\x12\x10\n\x08villa_id\x18\x01 \x01(\x04\x12\x0f\n\x07room_id\x18\x02 \x01(\x04\x12\x0b\n\x03uid\x18\x03 \x01(\x04\x12\x13\n\x0b\x65moticon_id\x18\x04 \x01(\r\x12\x10\n\x08\x65moticon\x18\x05 \x01(\t\x12\x0f\n\x07msg_uid\x18\x06 \x01(\t\x12\x11\n\tis_cancel\x18\x07 \x01(\x08\x12\x12\n\nbot_msg_id\x18\x08 \x01(\t\x12\x15\n\remoticon_type\x18\t \x01(\r\x1a\x87\x02\n\x11\x41uditCallbackInfo\x12\x10\n\x08\x61udit_id\x18\x01 \x01(\t\x12\x12\n\nbot_tpl_id\x18\x02 \x01(\t\x12\x10\n\x08villa_id\x18\x03 \x01(\x04\x12\x0f\n\x07room_id\x18\x04 \x01(\x04\x12\x0f\n\x07user_id\x18\x05 \x01(\x04\x12\x14\n\x0cpass_through\x18\x06 \x01(\t\x12S\n\x0c\x61udit_result\x18\x07 \x01(\x0e\x32=.vila_bot.RobotEvent.ExtendData.AuditCallbackInfo.AuditResult\"-\n\x0b\x41uditResult\x12\x08\n\x04None\x10\x00\x12\x08\n\x04Pass\x10\x01\x12\n\n\x06Reject\x10\x02\x1a\xa6\x01\n\x15\x43lickMsgComponentInfo\x12\x10\n\x08villa_id\x18\x01 \x01(\x04\x12\x0f\n\x07room_id\x18\x02 \x01(\x04\x12\x14\n\x0c\x63omponent_id\x18\x03 \x01(\t\x12\x0f\n\x07msg_uid\x18\x04 \x01(\t\x12\x0b\n\x03uid\x18\x05 \x01(\x04\x12\x12\n\nbot_msg_id\x18\x06 \x01(\t\x12\x13\n\x0btemplate_id\x18\x07 \x01(\x04\x12\r\n\x05\x65xtra\x18\x08 \x01(\tB\x0c\n\nevent_data\"\xa7\x01\n\tEventType\x12\x18\n\x14UnknowRobotEventType\x10\x00\x12\r\n\tJoinVilla\x10\x01\x12\x0f\n\x0bSendMessage\x10\x02\x12\x0f\n\x0b\x43reateRobot\x10\x03\x12\x0f\n\x0b\x44\x65leteRobot\x10\x04\x12\x14\n\x10\x41\x64\x64QuickEmoticon\x10\x05\x12\x11\n\rAuditCallback\x10\x06\x12\x15\n\x11\x43lickMsgComponent\x10\x07*b\n\x08RoomType\x12\x13\n\x0fRoomTypeInvalid\x10\x00\x12\x14\n\x10RoomTypeChatRoom\x10\x01\x12\x14\n\x10RoomTypePostRoom\x10\x02\x12\x15\n\x11RoomTypeSceneRoom\x10\x03*6\n\nObjectName\x12\x14\n\x10UnknowObjectName\x10\x00\x12\x08\n\x04Text\x10\x01\x12\x08\n\x04Post\x10\x02\x42\x36Z4gopkg.mihoyo.com/vila-bot-go/proto/vila_bot;vila_botb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'model_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z4gopkg.mihoyo.com/vila-bot-go/proto/vila_bot;vila_bot'
  _globals['_ROOMTYPE']._serialized_start=2644
  _globals['_ROOMTYPE']._serialized_end=2742
  _globals['_OBJECTNAME']._serialized_start=2744
  _globals['_OBJECTNAME']._serialized_end=2798
  _globals['_ROBOTTEMPLATE']._serialized_start=26
  _globals['_ROBOTTEMPLATE']._serialized_end=402
  _globals['_ROBOTTEMPLATE_PARAM']._serialized_start=251
  _globals['_ROBOTTEMPLATE_PARAM']._serialized_end=272
  _globals['_ROBOTTEMPLATE_COMMAND']._serialized_start=274
  _globals['_ROBOTTEMPLATE_COMMAND']._serialized_end=358
  _globals['_ROBOTTEMPLATE_CUSTOMSETTING']._serialized_start=360
  _globals['_ROBOTTEMPLATE_CUSTOMSETTING']._serialized_end=402
  _globals['_ROBOT']._serialized_start=404
  _globals['_ROBOT']._serialized_end=472
  _globals['_QUOTEMESSAGEINFO']._serialized_start=475
  _globals['_QUOTEMESSAGEINFO']._serialized_end=658
  _globals['_ROBOTEVENT']._serialized_start=661
  _globals['_ROBOTEVENT']._serialized_end=2642
  _globals['_ROBOTEVENT_EXTENDDATA']._serialized_start=857
  _globals['_ROBOTEVENT_EXTENDDATA']._serialized_end=2472
  _globals['_ROBOTEVENT_EXTENDDATA_JOINVILLAINFO']._serialized_start=1406
  _globals['_ROBOTEVENT_EXTENDDATA_JOINVILLAINFO']._serialized_end=1502
  _globals['_ROBOTEVENT_EXTENDDATA_SENDMESSAGEINFO']._serialized_start=1505
  _globals['_ROBOTEVENT_EXTENDDATA_SENDMESSAGEINFO']._serialized_end=1758
  _globals['_ROBOTEVENT_EXTENDDATA_CREATEROBOTINFO']._serialized_start=1760
  _globals['_ROBOTEVENT_EXTENDDATA_CREATEROBOTINFO']._serialized_end=1795
  _globals['_ROBOTEVENT_EXTENDDATA_DELETEROBOTINFO']._serialized_start=1797
  _globals['_ROBOTEVENT_EXTENDDATA_DELETEROBOTINFO']._serialized_end=1832
  _globals['_ROBOTEVENT_EXTENDDATA_ADDQUICKEMOTICONINFO']._serialized_start=1835
  _globals['_ROBOTEVENT_EXTENDDATA_ADDQUICKEMOTICONINFO']._serialized_end=2023
  _globals['_ROBOTEVENT_EXTENDDATA_AUDITCALLBACKINFO']._serialized_start=2026
  _globals['_ROBOTEVENT_EXTENDDATA_AUDITCALLBACKINFO']._serialized_end=2289
  _globals['_ROBOTEVENT_EXTENDDATA_AUDITCALLBACKINFO_AUDITRESULT']._serialized_start=2244
  _globals['_ROBOTEVENT_EXTENDDATA_AUDITCALLBACKINFO_AUDITRESULT']._serialized_end=2289
  _globals['_ROBOTEVENT_EXTENDDATA_CLICKMSGCOMPONENTINFO']._serialized_start=2292
  _globals['_ROBOTEVENT_EXTENDDATA_CLICKMSGCOMPONENTINFO']._serialized_end=2458
  _globals['_ROBOTEVENT_EVENTTYPE']._serialized_start=2475
  _globals['_ROBOTEVENT_EVENTTYPE']._serialized_end=2642
# @@protoc_insertion_point(module_scope)
