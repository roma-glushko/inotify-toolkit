from enum import IntEnum
from types import TracebackType
from typing import List, Optional

"""
The lib version
"""
__version__: str

class EventTypeAttributes(IntEnum):
    CREATED = 0b000000

class WatcherError(Exception):
    """Watcher Runtime Error"""

class Event:
    """
    """
    event_type: int
    detected_at_ns: int
    path: str

    def __init__(self, event_type: int, detected_at_ns: int, path: str) -> None:
        ...

class WatcherWrapper:
    """
    Watcher listens to filesystem events and retrieves them for the Notifier.
    By default, it tries to pick the most appropriate watching strategy that depends on your OS.
    If that's failed for some reason, it will try to fall back polling filesystem.
    """

    def __init__(
        self,
        debug: bool = False,
        force_polling: bool = False,
        poll_delay_ms: int = 50,
    ) -> None:
        """

        """
        ...

    def watch(self, paths: List[str], recursive: bool = True, ignore_permission_errors: bool = False) -> None:
        """

        """
        ...

    def unwatch(self, paths: List[str]) -> None:
        """
        """
        ...

    def get(self) -> Optional[RawEvent]:
        ...

    def close(self) -> None:
        """
        """
        ...

    def start(self) -> None:
        ...

    def stop(self) -> None:
        ...

# Main Event Groups

class EventType(IntEnum):
    CREATE = 0
    ACCESS = 1
    REMOVE = 2
    MODIFY = 3
    OTHER = 4

class ObjectType(IntEnum):
    FILE = 0
    DIR = 1
    OTHER = 3

class RawEvent:
    event_type: Optional[EventType]
    object_type: Optional[ObjectType]

    detected_at_ns: int
    path: str

class AccessEvent(Event):
    """
    """

class CreateEvent(Event):
    """
    """

    def is_file(self) -> bool:
        ...

    def is_dir(self) -> bool:
        ...

    def is_other(self) -> bool:
        ...

class RemoveEvent(Event):
    """
    """

    def is_file(self) -> bool:
        ...

    def is_dir(self) -> bool:
        ...

    def is_other(self) -> bool:
        ...

class ModifyEvent(Event):
    """
    """

class OtherEvent(Event):
    """
    An event not fitting in any of the above four categories.

    This may be used for meta-events about the watch itself
    """

# Access Events
class ReadEvent(AccessEvent):
    """
    """

class OpenEvent(AccessEvent):
    """
    """

class CloseEvent(AccessEvent):
    """
    """

# Create Events

class FileCreatedEvent(CreateEvent):
    """
    """

class DirCreatedEvent(CreateEvent):
    """
    """

class OtherCreatedEvent(CreateEvent):
    """
    """

# Remove Events

class FileRemovedEvent(RemoveEvent):
    """
    """

class DirRemovedEvent(RemoveEvent):
    """
    """

class OtherRemovedEvent(RemoveEvent):
    """
    """

# Modify Events

class DataChangedEvent(ModifyEvent):
    """
    """

class MetadataModifiedEvent(ModifyEvent):
    """
    """

class RenameEvent(ModifyEvent):
    """
    """


# Data Modified Events

class ContentChangedEvent(DataChangedEvent):
    """
    """

class SizeChangedEvent(DataChangedEvent):
    """
    """

class OtherDataChangedEvent(DataChangedEvent):
    """
    """

# Metadata Modified Events

class OwnershipModifiedEvent(MetadataModifiedEvent):
    """
    An event emitted when the ownership of the file or folder is changed
    """

class PermissionsModifiedEvent(MetadataModifiedEvent):
    """
    """

class WriteTimeModifiedEvent(MetadataModifiedEvent):
    """
    An event emitted when write or modify time of the file or folder is changed
    """

class AccessTimeModifiedEvent(MetadataModifiedEvent):
    """
    """

class ExtendedAttributeModifiedEvent(MetadataModifiedEvent):
    """
    """

class OtherAttributeModifiedEvent(MetadataModifiedEvent):
    """
    """

# Name Modified Events

class RenamedToEvent(RenameEvent):
    """
    """

class RenamedFromEvent(RenameEvent):
    """
    """

class RenamedBothEvent(RenameEvent):
    """
    """

class RenamedOtherEvent(RenameEvent):
    """
    """