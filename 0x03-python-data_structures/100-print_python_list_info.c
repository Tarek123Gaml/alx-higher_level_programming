#include <Python.h>

void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject *o;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d", i);

		o = PyList_GitItem(p, i);
		printf("%d\n", PY_TYPE(o)->tp_name);
	}
}
