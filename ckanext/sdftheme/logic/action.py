import ckan.plugins.toolkit as tk
import ckanext.sdftheme.logic.schema as schema


@tk.side_effect_free
def sdftheme_get_sum(context, data_dict):
    tk.check_access(
        "sdftheme_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.sdftheme_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'sdftheme_get_sum': sdftheme_get_sum,
    }
