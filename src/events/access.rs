use notify::event::{AccessKind, AccessMode as NotifyAccessMode};
use pyo3::prelude::*;
use std::convert::From;
use std::path::PathBuf;

#[derive(Debug)]
pub enum AccessType {
    Any = 0,
    Read = 1,
    Open = 2,
    Close = 3,
    Other = 4,
}

impl From<AccessKind> for AccessType {
    fn from(kind: AccessKind) -> Self {
        return match kind {
            AccessKind::Read => AccessType::Read,
            AccessKind::Open(_) => AccessType::Open,
            AccessKind::Close(_) => AccessType::Close,
            AccessKind::Other => AccessType::Other,
            AccessKind::Any => AccessType::Any,
        };
    }
}

#[derive(Debug)]
pub enum AccessMode {
    Any = 0,
    Read = 1,
    Write = 2,
    Execute = 3,
    Other = 4,
}

impl From<NotifyAccessMode> for AccessMode {
    fn from(kind: NotifyAccessMode) -> Self {
        return match kind {
            NotifyAccessMode::Read => AccessMode::Read,
            NotifyAccessMode::Write => AccessMode::Write,
            NotifyAccessMode::Execute => AccessMode::Execute,
            NotifyAccessMode::Other => AccessMode::Other,
            NotifyAccessMode::Any => AccessMode::Any,
        };
    }
}

#[derive(Debug)]
pub enum MetadataType {
    AccessTime = 0,
    WriteTime = 1,
    Ownership = 2,
    Permissions = 3,
    Extended = 4,
    Other = 5,
    Any = 6,
}

#[pyclass]
#[derive(Debug)]
pub(crate) struct AccessEvent {
    detected_at_ns: u128,
    path: PathBuf,
    access_type: AccessType,
    access_mode: Option<AccessMode>,
}

impl AccessEvent {
    pub fn new(detected_at_ns: u128, path: PathBuf, access_kind: AccessKind) -> Self {
        let access_mode: Option<AccessMode> = match access_kind {
            AccessKind::Open(access_mode) => Some(AccessMode::from(access_mode)),
            AccessKind::Close(access_mode) => Some(AccessMode::from(access_mode)),
            _ => None,
        };

        Self {
            detected_at_ns,
            path,
            access_type: AccessType::from(access_kind),
            access_mode,
        }
    }
}