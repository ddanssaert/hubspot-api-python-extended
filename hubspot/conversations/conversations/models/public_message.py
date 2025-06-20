# coding: utf-8

"""
    Conversations Inbox & Messages

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
from hubspot.conversations.conversations.models.public_assignment_message import PublicAssignmentMessage
from hubspot.conversations.conversations.models.public_comment import PublicComment
from hubspot.conversations.conversations.models.public_conversations_message import PublicConversationsMessage
from hubspot.conversations.conversations.models.public_thread_inbox_change import PublicThreadInboxChange
from hubspot.conversations.conversations.models.public_thread_status_change import PublicThreadStatusChange
from hubspot.conversations.conversations.models.public_welcome_message import PublicWelcomeMessage
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

PUBLICMESSAGE_ONE_OF_SCHEMAS = ["PublicAssignmentMessage", "PublicComment", "PublicConversationsMessage", "PublicThreadInboxChange", "PublicThreadStatusChange", "PublicWelcomeMessage"]

class PublicMessage(BaseModel):
    """
    PublicMessage
    """
    # data type: PublicConversationsMessage
    oneof_schema_1_validator: Optional[PublicConversationsMessage] = None
    # data type: PublicComment
    oneof_schema_2_validator: Optional[PublicComment] = None
    # data type: PublicWelcomeMessage
    oneof_schema_3_validator: Optional[PublicWelcomeMessage] = None
    # data type: PublicAssignmentMessage
    oneof_schema_4_validator: Optional[PublicAssignmentMessage] = None
    # data type: PublicThreadStatusChange
    oneof_schema_5_validator: Optional[PublicThreadStatusChange] = None
    # data type: PublicThreadInboxChange
    oneof_schema_6_validator: Optional[PublicThreadInboxChange] = None
    actual_instance: Optional[Union[PublicAssignmentMessage, PublicComment, PublicConversationsMessage, PublicThreadInboxChange, PublicThreadStatusChange, PublicWelcomeMessage]] = None
    one_of_schemas: Set[str] = { "PublicAssignmentMessage", "PublicComment", "PublicConversationsMessage", "PublicThreadInboxChange", "PublicThreadStatusChange", "PublicWelcomeMessage" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
    }

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
        instance = PublicMessage.model_construct()
        error_messages = []
        match = 0
        # validate data type: PublicConversationsMessage
        if not isinstance(v, PublicConversationsMessage):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PublicConversationsMessage`")
        else:
            match += 1
        # validate data type: PublicComment
        if not isinstance(v, PublicComment):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PublicComment`")
        else:
            match += 1
        # validate data type: PublicWelcomeMessage
        if not isinstance(v, PublicWelcomeMessage):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PublicWelcomeMessage`")
        else:
            match += 1
        # validate data type: PublicAssignmentMessage
        if not isinstance(v, PublicAssignmentMessage):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PublicAssignmentMessage`")
        else:
            match += 1
        # validate data type: PublicThreadStatusChange
        if not isinstance(v, PublicThreadStatusChange):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PublicThreadStatusChange`")
        else:
            match += 1
        # validate data type: PublicThreadInboxChange
        if not isinstance(v, PublicThreadInboxChange):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PublicThreadInboxChange`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in PublicMessage with oneOf schemas: PublicAssignmentMessage, PublicComment, PublicConversationsMessage, PublicThreadInboxChange, PublicThreadStatusChange, PublicWelcomeMessage. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in PublicMessage with oneOf schemas: PublicAssignmentMessage, PublicComment, PublicConversationsMessage, PublicThreadInboxChange, PublicThreadStatusChange, PublicWelcomeMessage. Details: " + ", ".join(error_messages))
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

        # deserialize data into PublicConversationsMessage
        try:
            instance.actual_instance = PublicConversationsMessage.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PublicComment
        try:
            instance.actual_instance = PublicComment.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PublicWelcomeMessage
        try:
            instance.actual_instance = PublicWelcomeMessage.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PublicAssignmentMessage
        try:
            instance.actual_instance = PublicAssignmentMessage.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PublicThreadStatusChange
        try:
            instance.actual_instance = PublicThreadStatusChange.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PublicThreadInboxChange
        try:
            instance.actual_instance = PublicThreadInboxChange.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into PublicMessage with oneOf schemas: PublicAssignmentMessage, PublicComment, PublicConversationsMessage, PublicThreadInboxChange, PublicThreadStatusChange, PublicWelcomeMessage. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into PublicMessage with oneOf schemas: PublicAssignmentMessage, PublicComment, PublicConversationsMessage, PublicThreadInboxChange, PublicThreadStatusChange, PublicWelcomeMessage. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], PublicAssignmentMessage, PublicComment, PublicConversationsMessage, PublicThreadInboxChange, PublicThreadStatusChange, PublicWelcomeMessage]]:
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


