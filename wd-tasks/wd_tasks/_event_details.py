from __future__ import annotations

from typing import Annotated

from pydantic import Field
from wt_registry import register

from ecoscope.platform.tasks.io._earthranger import (
    AnalysisFieldAnnotation,
    AnalysisFieldLabelAnnotation,
    AnalysisFieldUnitAnnotation,
    CategoryFieldAnnotation,
    CategoryFieldLabelAnnotation,
    CombinedEventsAndDetailsParams,
    DefaultEventColumns,
    EventColumnsAnnotation,
    IncludeDetailsAnnotation,
    IncludeDisplayValuesAnnotation,
    IncludeNullGeometryAnnotation,
    IncludeRelatedEventsAnnotation,
    IncludeUpdatesAnnotation,
    RaiseOnEmptyAnnotation,
    TimeRangeAnnotation,
)


@register()
def set_optional_event_details_params(
    client: str,
    time_range: TimeRangeAnnotation,
    event_type: Annotated[str, Field(title="Events Type", default="")] = "",
    analysis_field: AnalysisFieldAnnotation = "",
    analysis_field_label: AnalysisFieldLabelAnnotation = "",
    analysis_field_unit: AnalysisFieldUnitAnnotation = "",
    event_columns: EventColumnsAnnotation = DefaultEventColumns,
    category_field: CategoryFieldAnnotation = "",
    category_field_label: CategoryFieldLabelAnnotation = "",
    include_null_geometry: IncludeNullGeometryAnnotation = True,
    raise_on_empty: RaiseOnEmptyAnnotation = True,
    include_details: IncludeDetailsAnnotation = True,
    include_updates: IncludeUpdatesAnnotation = False,
    include_related_events: IncludeRelatedEventsAnnotation = False,
    include_display_values: IncludeDisplayValuesAnnotation = False,
) -> Annotated[
    CombinedEventsAndDetailsParams | None,
    Field(description="Event details params, or None to skip this section"),
]:
    if not event_type:
        return None
    return CombinedEventsAndDetailsParams(
        client=client,
        time_range=time_range,
        event_type=event_type,
        event_columns=event_columns,
        analysis_field=analysis_field,
        analysis_field_label=analysis_field_label,
        analysis_field_unit=analysis_field_unit,
        category_field=category_field,
        category_field_label=category_field_label,
        include_null_geometry=include_null_geometry,
        raise_on_empty=raise_on_empty,
        include_details=include_details,
        include_updates=include_updates,
        include_related_events=include_related_events,
        include_display_values=include_display_values,
    )
