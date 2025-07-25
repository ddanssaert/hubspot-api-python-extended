# coding: utf-8

"""
    Conversations Custom Channels

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from hubspot.conversations.custom_channels.models.contact_attachment import ContactAttachment
from hubspot.conversations.custom_channels.models.file_attachment import FileAttachment
from hubspot.conversations.custom_channels.models.location_attachment import LocationAttachment
from hubspot.conversations.custom_channels.models.message_header_attachment import MessageHeaderAttachment
from hubspot.conversations.custom_channels.models.quick_replies_attachment import QuickRepliesAttachment
from hubspot.conversations.custom_channels.models.unsupported_content_attachment import UnsupportedContentAttachment
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

CHANNELINTEGRATIONMESSAGEEGGATTACHMENTSINNER_ONE_OF_SCHEMAS = ["ContactAttachment", "FileAttachment", "LocationAttachment", "MessageHeaderAttachment", "QuickRepliesAttachment", "UnsupportedContentAttachment"]

class ChannelIntegrationMessageEggAttachmentsInner(BaseModel):
    """
    ChannelIntegrationMessageEggAttachmentsInner
    """
    # data type: FileAttachment
    oneof_schema_1_validator: Optional[FileAttachment] = None
    # data type: LocationAttachment
    oneof_schema_2_validator: Optional[LocationAttachment] = None
    # data type: ContactAttachment
    oneof_schema_3_validator: Optional[ContactAttachment] = None
    # data type: UnsupportedContentAttachment
    oneof_schema_4_validator: Optional[UnsupportedContentAttachment] = None
    # data type: MessageHeaderAttachment
    oneof_schema_5_validator: Optional[MessageHeaderAttachment] = None
    # data type: QuickRepliesAttachment
    oneof_schema_6_validator: Optional[QuickRepliesAttachment] = None
    actual_instance: Optional[Union[ContactAttachment, FileAttachment, LocationAttachment, MessageHeaderAttachment, QuickRepliesAttachment, UnsupportedContentAttachment]] = None
    one_of_schemas: Set[str] = { "ContactAttachment", "FileAttachment", "LocationAttachment", "MessageHeaderAttachment", "QuickRepliesAttachment", "UnsupportedContentAttachment" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = ChannelIntegrationMessageEggAttachmentsInner.model_construct()
        error_messages = []
        match = 0
        # validate data type: FileAttachment
        if not isinstance(v, FileAttachment):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FileAttachment`")
        else:
            match += 1
        # validate data type: LocationAttachment
        if not isinstance(v, LocationAttachment):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LocationAttachment`")
        else:
            match += 1
        # validate data type: ContactAttachment
        if not isinstance(v, ContactAttachment):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ContactAttachment`")
        else:
            match += 1
        # validate data type: UnsupportedContentAttachment
        if not isinstance(v, UnsupportedContentAttachment):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UnsupportedContentAttachment`")
        else:
            match += 1
        # validate data type: MessageHeaderAttachment
        if not isinstance(v, MessageHeaderAttachment):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MessageHeaderAttachment`")
        else:
            match += 1
        # validate data type: QuickRepliesAttachment
        if not isinstance(v, QuickRepliesAttachment):
            error_messages.append(f"Error! Input type `{type(v)}` is not `QuickRepliesAttachment`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ChannelIntegrationMessageEggAttachmentsInner with oneOf schemas: ContactAttachment, FileAttachment, LocationAttachment, MessageHeaderAttachment, QuickRepliesAttachment, UnsupportedContentAttachment. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ChannelIntegrationMessageEggAttachmentsInner with oneOf schemas: ContactAttachment, FileAttachment, LocationAttachment, MessageHeaderAttachment, QuickRepliesAttachment, UnsupportedContentAttachment. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into FileAttachment
        try:
            instance.actual_instance = FileAttachment.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into LocationAttachment
        try:
            instance.actual_instance = LocationAttachment.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ContactAttachment
        try:
            instance.actual_instance = ContactAttachment.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UnsupportedContentAttachment
        try:
            instance.actual_instance = UnsupportedContentAttachment.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into MessageHeaderAttachment
        try:
            instance.actual_instance = MessageHeaderAttachment.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into QuickRepliesAttachment
        try:
            instance.actual_instance = QuickRepliesAttachment.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ChannelIntegrationMessageEggAttachmentsInner with oneOf schemas: ContactAttachment, FileAttachment, LocationAttachment, MessageHeaderAttachment, QuickRepliesAttachment, UnsupportedContentAttachment. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ChannelIntegrationMessageEggAttachmentsInner with oneOf schemas: ContactAttachment, FileAttachment, LocationAttachment, MessageHeaderAttachment, QuickRepliesAttachment, UnsupportedContentAttachment. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], ContactAttachment, FileAttachment, LocationAttachment, MessageHeaderAttachment, QuickRepliesAttachment, UnsupportedContentAttachment]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


