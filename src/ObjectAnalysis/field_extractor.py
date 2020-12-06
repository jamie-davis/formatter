def get_keys(value_pairs):
    return [pair for pair in value_pairs]


def primitive_dict(item):
    result = dict()
    result[None] = item
    return result


def get_values(item):
    if hasattr(item, '__dict__'):
        return vars(item)

    if isinstance(item, dict):
        return item

    return primitive_dict(item)


class FieldExtractor:
    """Extracts the fields present on a collection of objects."""

    @staticmethod
    def extract(items):
        """Analyse a list of objects and return a FieldExtractor instance containing the result"""
        type_name = type(items).__name__
        if type_name != "list" and type_name != "tuple":
            items = [items]

        all_values = [get_values(item) for item in items]

        extract = FieldExtractor()

        all_keys = [key for valuePairs in all_values for key in valuePairs]
        extract.keys = list(dict.fromkeys(all_keys))
        extract.rows = all_values
        return extract
