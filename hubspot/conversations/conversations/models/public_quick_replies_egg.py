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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from hubspot.conversations.conversations.models.quick_reply import QuickReply
from typing import Optional, Set
from typing_extensions import Self

class PublicQuickRepliesEgg(BaseModel):
    """
    PublicQuickRepliesEgg
    """ # noqa: E501
    quick_replies: List[QuickReply] = Field(alias="quickReplies")
    type: StrictStr
    __properties: ClassVar[List[str]] = ["quickReplies", "type"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['QUICK_REPLIES']):
            raise ValueError("must be one of enum values ('QUICK_REPLIES')")
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
        """Create an instance of PublicQuickRepliesEgg from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in quick_replies (list)
        _items = []
        if self.quick_replies:
            for _item_quick_replies in self.quick_replies:
                if _item_quick_replies:
                    _items.append(_item_quick_replies.to_dict())
            _dict['quickReplies'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PublicQuickRepliesEgg from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "quickReplies": [QuickReply.from_dict(_item) for _item in obj["quickReplies"]] if obj.get("quickReplies") is not None else None,
            "type": obj.get("type") if obj.get("type") is not None else 'QUICK_REPLIES'
        })
        return _obj


