import logging
import os.path


class log:
    def __init__(self, nombreLogger):
        # create logger
        self.logger = logging.getLogger(nombreLogger)
        self.logger.filename = 'app.log'
        self.logger.setLevel(logging.DEBUG)
        # create console handler and set level to debug
        ch = logging.FileHandler("app.log", mode='a')
        ch.setLevel(logging.DEBUG)
        # create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # add formatter to ch
        ch.setFormatter(formatter)
        # add ch to logger
        self.logger.addHandler(ch)

    def debug(self, mensaje):
        self.logger.debug(mensaje)

    def info(self, mensaje):
        self.logger.info(mensaje)

    def warning(self, mensaje):
        self.logger.warning(mensaje)

    def error(self, mensaje):
        self.logger.error(mensaje)

    def critical(self, mensaje):
        self.logger.critical(mensaje)

class fileManager:
    logD = log("fileManager")

    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo
    
    def CrearArchivo(self):
        try:
            directorioActual = os.getcwd()
            path = directorioActual+"\\"+self.nombreArchivo
            if os.path.isfile(path):
                pass
            else:
                file = open(self.nombreArchivo,'w')
                file.write("[]")
        except Exception as e:
            return e

    def leerArchivo(self):
        try:
            directorioActual = os.getcwd()
            path = directorioActual+"\\"+self.nombreArchivo
            self.logD.debug(path)
            if os.path.isfile(path):
                file = open(self.nombreArchivo,'r')
                return file.read()
            else:
                file = open(self.nombreArchivo,'w')
                file.close()
                file = open(self.nombreArchivo, 'a')
                file.write("[]")
        except Exception as e:
            return e

    def escribirArchivo(self, linea):
        try:
            directorioActual = os.getcwd()
            path = directorioActual+"\\"+self.nombreArchivo
            self.logD.debug(path)
            if(os.path.isfile(path)):
                try:
                    #escribir el archiv
                    file = open(self.nombreArchivo, 'w')
                    file.write(linea + "\n")
                except Exception as e:
                    self.logD.error(e)
                finally:
                    file.close()
            else:
                file = open(self.nombreArchivo, 'w')
                file.close()
                file = open(self.nombreArchivo, 'a')
                file.write(linea + "\n")
        except Exception as error:
            self.logD.error(error)