import json

from django.conf import settings
from django.utils.translation import ugettext as _

from jsonobject.exceptions import BadValueError

from corehq.apps.userreports.exceptions import BadSpecError
from corehq.apps.userreports.reports.specs import (
    AggregateDateColumn,
    ConditionalAggregationColumn,
    ExpandedColumn,
    ExpressionColumn,
    FieldColumn,
    LocationColumn,
    MultibarAggregateChartSpec,
    MultibarChartSpec,
    OrderBySpec,
    PercentageColumn,
    PieChartSpec,
    SumWhenColumn,
)


class ReportColumnFactory(object):
    class_map = {
        'aggregate_date': AggregateDateColumn,
        'conditional_aggregation': ConditionalAggregationColumn,
        'sum_when': SumWhenColumn,
        'expanded': ExpandedColumn,
        'field': FieldColumn,
        'percent': PercentageColumn,
        'location': LocationColumn,
        'expression': ExpressionColumn,
    }

    @classmethod
    def from_spec(cls, spec, is_static):
        column_type = spec.get('type') or 'field'
        if column_type not in cls.class_map:
            raise BadSpecError(
                'Unknown or missing column type: {} must be in [{}]'.format(
                    column_type,
                    ', '.join(cls.class_map)
                )
            )
        column_class = cls.class_map[column_type]
        if column_class.restricted_to_static() and not (is_static or settings.UNIT_TESTING):
            raise BadSpecError("{} columns are only available to static report configs"
                               .format(column_type))
        try:
            return column_class.wrap(spec)
        except BadValueError as e:
            raise BadSpecError(_(
                'Problem creating column from spec: {}, message is: {}'
            ).format(
                json.dumps(spec, indent=2),
                str(e),
            ))


class ChartFactory(object):
    spec_map = {
        'pie': PieChartSpec,
        'multibar': MultibarChartSpec,
        'multibar-aggregate': MultibarAggregateChartSpec,
    }

    @classmethod
    def from_spec(cls, spec):
        if spec.get('type') not in cls.spec_map:
            raise BadSpecError(_('Illegal chart type: {0}, must be one of the following choice: ({1})').format(
                spec.get('type', _('(missing from spec)')),
                ', '.join(cls.spec_map)
            ))
        try:
            return cls.spec_map[spec['type']].wrap(spec)
        except BadValueError as e:
            raise BadSpecError(_('Problem creating chart from spec: {}, message is: {}').format(
                json.dumps(spec, indent=2),
                str(e),
            ))


class ReportOrderByFactory(object):

    @classmethod
    def from_spec(cls, spec):
        return OrderBySpec.wrap(spec)
