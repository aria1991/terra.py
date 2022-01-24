"""ibc client module data objects."""
from __future__ import annotations

from typing import List

import attr
from terra_proto.ibc.core.client.v1 import (
    Height as Height_pb,
    IdentifiedClientState as IdentifiedClientState_pb,
    ClientConsensusStates as ClientConsensusStates_pb,
    ConsensusStateWithHeight as ConsensusStateWithHeight_pb,
    Params as Params_pb
)
from betterproto.lib.google.protobuf import Any as Any_pb

from terra_sdk.util.json import JSONSerializable

__all__ = ["Height", "IdentifiedClientState", "ConsensusStateWithHeight", "ClientConsensusStates", "Params"]


@attr.s
class Height(JSONSerializable):
    revision_number: int = attr.ib(converter=int)
    revision_height: int = attr.ib(converter=int)

    def to_amino(self):
        raise Exception("Amino not supported")

    @classmethod
    def from_data(cls, data: dict) -> Height:
        return cls(
            revision_number=data["revision_number"],
            revision_height=data["revision_height"],
        )

    def to_proto(self) -> Height_pb:
        return Height_pb(
            revision_number=self.revision_number, revision_height=self.revision_height
        )

@attr.s
class IdentifiedClientState(JSONSerializable):
    """
    IdentifiedClientState defines a client state with an additional client identifier field.
    """

    client_id: str = attr.ib()
    client_state: Any_pb = attr.ib()

    def to_amino(self):
        raise Exception("Amino not supported")

    @classmethod
    def from_data(cls, data: dict) -> IdentifiedClientState:
        return cls(
            client_id=data["client_id"],
            consensus_state=Any_pb.FromString(data["client_state"])
        )

    def to_proto(self) -> IdentifiedClientState_pb:
        return IdentifiedClientState_pb(
            client_id=self.client_id,
            client_state=self.consensus_state
        )


@attr.s
class ConsensusStateWithHeight(JSONSerializable):
    """
    ConsensusStateWithHeight defines a consensus state with an additional height field.
    """

    height: str = attr.ib()
    consensus_state: Any_pb = attr.ib()

    def to_amino(self):
        raise Exception("Amino not supported")

    @classmethod
    def from_data(cls, data: dict) -> ConsensusStateWithHeight:
        return cls(
            height=data["height"],
            consensus_state=Any_pb.FromString(data["consensus_state"])
        )

    def to_proto(self) -> ConsensusStateWithHeight_pb:
        return ConsensusStateWithHeight_pb(
            height=self.height,
            consensus_state=self.consensus_state
        )


@attr.s
class ClientConsensusStates(JSONSerializable):
    """
    ClientConsensusStates defines all the stored consensus states for a given client.
    """

    client_id: str = attr.ib()
    consensus_states: List[ConsensusStateWithHeight] = attr.ib(converter=list)

    def to_amino(self):
        raise Exception("Amino not supported")

    @classmethod
    def from_data(cls, data: dict) -> ClientConsensusStates:
        return cls(
            client_id=data["client_id"],
            consensus_states=[ConsensusStateWithHeight.from_data(state) for state in data["consensus_states"]]
        )

    def to_proto(self) -> ClientConsensusStates_pb:
        return ClientConsensusStates_pb(
            client_id=self.client_id,
            consensus_states=[state.to_proto for state in self.consensus_states]
        )



@attr.s
class Params(JSONSerializable):
    """
    Params defines the set of IBC light client parameters.
    """

    allowed_clients: List[str] = attr.ib(converter=list)

    def to_amino(self):
        raise Exception("Amino not supported")

    @classmethod
    def from_data(cls, data: dict) -> Params:
        return cls(
            allowed_clients=data["allowed_clients"]
        )

    def to_proto(self) -> Params_pb:
        return Params_pb(
            allowed_clients=self.allowed_clients
        )
