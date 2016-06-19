#include <Python.h>

#include "MyDHT_RPi_Driver/dht_driver.h"

static PyObject *sensor_read(PyObject *self, PyObject *args) {
    int sensor_type, gpio_pin;
    int result;

    if (!PyArg_ParseTuple(args, "ii", &sensor_type, &gpio_pin))
        return NULL;

    struct dht_sensor_data data;
    result = dht_read(sensor_type, gpio_pin, &data);
    if(result < 0)
        data.humidity = data.temperature = 0.0f;

    return Py_BuildValue("iff", result, data.humidity, data.temperature);
}

static PyMethodDef DHTMethods[] = {
    {"_dht_read", sensor_read, METH_VARARGS, "Read sensor data!"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef mypydhtmodule = {
    PyModuleDef_HEAD_INIT,
    "dht_driver",  /* name of module */
    NULL,       /* module documentation, may be NULL */
    -1,         /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */
    DHTMethods
};

PyMODINIT_FUNC PyInit_dht_driver(void) {
    return PyModule_Create(&mypydhtmodule);
}