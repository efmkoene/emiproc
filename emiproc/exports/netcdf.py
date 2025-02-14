from datetime import datetime

NetcdfAttributes = dict[str, str]

def nc_cf_attributes(
    author: str,
    contact: str,
    title: str,
    source: str,
    comment: str = "",
    institution: str = "Empa, Swiss Federal Laboratories for Materials Science and Technology",
    history: str = "",
    references: str = "Produced by emiproc.",
    additional_attributes: NetcdfAttributes = {},
) ->  NetcdfAttributes :
    """Create attributes for a nc file based on cf conventions.


    Most of the following instructions at
    https://cfconventions.org/Data/cf-conventions/cf-conventions-1.10/cf-conventions.html#_attributes

    Some additional fields to the cf-conventions (author, contact)
    are added for simplifying data sharing.

    :param author: The author of the file.
    :param contact: The contact address (email) of a person that can be contacted
        if one has questions about the file.
    :param title:
        A succinct description of what is in the dataset.
    :param institution:
        Specifies where the original data was produced.
    :param source:
        The method of production of the original data. If it was model-generated, source should name the model and its version, as specifically as could be useful. If it is observational, source should characterize it (e.g., "surface observation" or "radiosonde").
    :param history:
        Provides an audit trail for modifications to the original data.
        Well-behaved generic netCDF filters will automatically append their name and the parameters with which they were invoked to the global history attribute of an input netCDF file
        We recommend that each line begin with a timestamp indicating the date and time of day that the program was executed.
    :param references:
        Published or web-based references that describe the data or methods used to produce it.
    :param comment:
        Miscellaneous information about the data or methods used to produce it.
    :param additional_attributes:
        Any attribute you want to add to the netcdf file produced.

    """
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {
        "Conventions": "CF-1.10",
        "title": title,
        "comment": comment,
        "source": source,
        "history": dt + ': created by emiproc ;\n' + history,
        "references": references,
        "institution": institution,
        "author": author,
        "contact": contact,
        "creation_time": dt,
        **additional_attributes,
    }
