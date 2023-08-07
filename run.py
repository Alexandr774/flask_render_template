from flask import Flask, render_template
from app.blueprint_tape.views import main_blueprint
import logging

logging.basicConfig(level=logging.DEBUG, filename='logs.log', filemode='w',
                    format="%(asctime)s %(levelname)s %(message)s")
logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")


app = Flask(__name__)

app.register_blueprint(main_blueprint)

@app.errorhandler(404)
def internal_error(error):
    logging.DEBUG('страница не найдена')
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    logging.CRITICAL('неверные данные')
    logging.exception()
    return render_template('500.html'), 500


# respons = app.test_client().get('/')
#
# assert respons.status_code == 200, 'erorr'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
