from dataclasses import dataclass
from typing import Optional

from openapi_core.casting.schemas.factories import SchemaCastersFactory
from openapi_core.deserializing.media_types import (
    media_type_deserializers_factory,
)
from openapi_core.deserializing.media_types.datatypes import (
    MediaTypeDeserializersDict,
)
from openapi_core.deserializing.media_types.factories import (
    MediaTypeDeserializersFactory,
)
from openapi_core.deserializing.styles import style_deserializers_factory
from openapi_core.deserializing.styles.factories import (
    StyleDeserializersFactory,
)
from openapi_core.validation.schemas.datatypes import FormatValidatorsDict
from openapi_core.validation.schemas.factories import SchemaValidatorsFactory


@dataclass
class ValidatorConfig:
    """Validator configuration dataclass.

    Attributes:
        server_base_url
            Server base URI.
        style_deserializers_factory
            Style deserializers factory.
        media_type_deserializers_factory
            Media type deserializers factory.
        schema_casters_factory
            Schema casters factory.
        schema_validators_factory
            Schema validators factory.
        extra_format_validators
            Extra format validators.
        extra_media_type_deserializers
            Extra media type deserializers.
    """

    server_base_url: Optional[str] = None

    style_deserializers_factory: StyleDeserializersFactory = (
        style_deserializers_factory
    )
    media_type_deserializers_factory: MediaTypeDeserializersFactory = (
        media_type_deserializers_factory
    )
    schema_casters_factory: Optional[SchemaCastersFactory] = None
    schema_validators_factory: Optional[SchemaValidatorsFactory] = None

    extra_format_validators: Optional[FormatValidatorsDict] = None
    extra_media_type_deserializers: Optional[MediaTypeDeserializersDict] = None
