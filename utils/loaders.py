#!/usr/bin/env python

import pandas as pd
import codecs
try:
    from StringIO import StringIO
except:
    from io import StringIO
import dateutil
import os, sys
import warnings

warnings.simplefilter(action="ignore", category=pd.io.common.DtypeWarning)
warnings.simplefilter(action="ignore", category=UserWarning)

def clean_date(date_string):
    try:
        return dateutil.parser.parse(date_string)
    except:
        return None

def load_file(file_path, **kwargs):
    with codecs.open(file_path, "r", encoding="latin-1") as f:
        # Remove NULL bytes from raw CSV
        denulled = f.read().replace("\x00", "").replace('"', "")
	denulled_io = StringIO(denulled)
        dataframe = pd.read_csv(denulled_io,
            sep = "\t", 
            na_values = ["N/A", "", " ", "  "],
            error_bad_lines = False,
            encoding="latin-1",
            **kwargs)
    return dataframe
