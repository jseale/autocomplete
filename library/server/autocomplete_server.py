""" Template for autocomplete server. """
import os
import sys
from flask import Flask, request, jsonify

#Get package prefix; insert autocomplete on path for import
AUTOC = os.path.abspath(__file__ + "/../../../")
sys.path.insert(0, "{}/library".format(AUTOC))
from autocomplete import autocompleter
from log_setup import log_setup
logger = log_setup('server')

app = Flask(__name__)

#TO DO: Encode text as string, not bytes throughout code
#to avoid decoding here for jsonify.
@app.route('/autocomplete')
def autocomplete():
    """ Generate autocompletions given the query 'q' """
    try:
        q = request.args.get('q')
    except Exception as e:
        logger.exception(str(e))
    try:
        completions = my_autocompleter.generate_completions(q)
    except Exception as e:
        logger.exception(str(e))
    try:
        completions_converted = \
                [completion.decode("utf-8") for completion in completions]
        return jsonify({"Completions": completions_converted})
    except Exception as e:
        logger.exception(str(e))

if __name__ == "__main__":
    my_autocompleter = autocompleter.Autocompleter()
    app.run()
