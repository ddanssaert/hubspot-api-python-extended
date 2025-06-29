# coding: utf-8

"""
    Conversations Inbox & Messages

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from hubspot.conversations.conversations.models.public_thread_associations import PublicThreadAssociations
from typing import Optional, Set
from typing_extensions import Self

class PublicThread(BaseModel):
    """
    PublicThread
    """ # noqa: E501
    associated_contact_id: StrictStr = Field(description="The ID of the associated Contact in the CRM. If the Contact for the thread has not yet been added or created, the `associatedContactId` returned will be a visitorID and cannot be used to search for the Contact in the CRM", alias="associatedContactId")
    thread_associations: Optional[PublicThreadAssociations] = Field(default=None, alias="threadAssociations")
    assigned_to: Optional[StrictStr] = Field(default=None, alias="assignedTo")
    created_at: datetime = Field(description="When the thread was created.", alias="createdAt")
    archived: Optional[StrictBool] = Field(default=None, description="Whether this thread is archived.")
    original_channel_id: StrictStr = Field(alias="originalChannelId")
    latest_message_timestamp: Optional[datetime] = Field(default=None, description="The time that the latest message was sent or received on the thread.", alias="latestMessageTimestamp")
    latest_message_sent_timestamp: Optional[datetime] = Field(default=None, description="The time that the latest message was sent on the thread.", alias="latestMessageSentTimestamp")
    original_channel_account_id: StrictStr = Field(alias="originalChannelAccountId")
    id: StrictStr = Field(description="The unique ID of the thread.")
    closed_at: Optional[datetime] = Field(default=None, description="When the thread was closed. Only set if the thread is closed.", alias="closedAt")
    spam: StrictBool = Field(description="Whether the thread is marked as spam.")
    inbox_id: StrictStr = Field(description="The ID of the conversations inbox containing the thread.", alias="inboxId")
    status: StrictStr = Field(description="The thread's status: `OPEN` or `CLOSED`.")
    latest_message_received_timestamp: Optional[datetime] = Field(default=None, description="The time that the latest message was sent on the thread.", alias="latestMessageReceivedTimestamp")
    __properties: ClassVar[List[str]] = ["associatedContactId", "threadAssociations", "assignedTo", "createdAt", "archived", "originalChannelId", "latestMessageTimestamp", "latestMessageSentTimestamp", "originalChannelAccountId", "id", "closedAt", "spam", "inboxId", "status", "latestMessageReceivedTimestamp"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['OPEN', 'CLOSED']):
            raise ValueError("must be one of enum values ('OPEN', 'CLOSED')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PublicThread from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of thread_associations
        if self.thread_associations:
            _dict['threadAssociations'] = self.thread_associations.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PublicThread from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "associatedContactId": obj.get("associatedContactId"),
            "threadAssociations": PublicThreadAssociations.from_dict(obj["threadAssociations"]) if obj.get("threadAssociations") is not None else None,
            "assignedTo": obj.get("assignedTo"),
            "createdAt": obj.get("createdAt"),
            "archived": obj.get("archived"),
            "originalChannelId": obj.get("originalChannelId"),
            "latestMessageTimestamp": obj.get("latestMessageTimestamp"),
            "latestMessageSentTimestamp": obj.get("latestMessageSentTimestamp"),
            "originalChannelAccountId": obj.get("originalChannelAccountId"),
            "id": obj.get("id"),
            "closedAt": obj.get("closedAt"),
            "spam": obj.get("spam"),
            "inboxId": obj.get("inboxId"),
            "status": obj.get("status"),
            "latestMessageReceivedTimestamp": obj.get("latestMessageReceivedTimestamp")
        })
        return _obj


