# -*- coding: UTF-8 -*-
# Code generated by lark suite oapi sdk gen

from typing import List, Dict, Any
import attr




@attr.s
class FileConfig(object):
    file_id = attr.ib(type=str, default=None, metadata={'json': 'file_id'})
    format = attr.ib(type=str, default=None, metadata={'json': 'format'})
    engine_type = attr.ib(type=str, default=None, metadata={'json': 'engine_type'})


@attr.s
class StreamConfig(object):
    stream_id = attr.ib(type=str, default=None, metadata={'json': 'stream_id'})
    sequence_id = attr.ib(type=int, default=None, metadata={'json': 'sequence_id'})
    action = attr.ib(type=int, default=None, metadata={'json': 'action'})
    format = attr.ib(type=str, default=None, metadata={'json': 'format'})
    engine_type = attr.ib(type=str, default=None, metadata={'json': 'engine_type'})


@attr.s
class Speech(object):
    speech = attr.ib(type=str, default=None, metadata={'json': 'speech'})
    speech_key = attr.ib(type=str, default=None, metadata={'json': 'speech_key'})



@attr.s
class SpeechFileRecognizeReqBody(object):
    speech = attr.ib(type=Speech, default=None, metadata={'json': 'speech'})
    config = attr.ib(type=FileConfig, default=None, metadata={'json': 'config'})


@attr.s
class SpeechFileRecognizeResult(object):
    recognition_text = attr.ib(type=str, default=None, metadata={'json': 'recognition_text'})


@attr.s
class SpeechStreamRecognizeReqBody(object):
    speech = attr.ib(type=Speech, default=None, metadata={'json': 'speech'})
    config = attr.ib(type=StreamConfig, default=None, metadata={'json': 'config'})


@attr.s
class SpeechStreamRecognizeResult(object):
    stream_id = attr.ib(type=str, default=None, metadata={'json': 'stream_id'})
    sequence_id = attr.ib(type=int, default=None, metadata={'json': 'sequence_id'})
    recognition_text = attr.ib(type=str, default=None, metadata={'json': 'recognition_text'})