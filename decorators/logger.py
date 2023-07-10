# import datetime
#
#
# class CountCalls:
#     def __init__(self, func):
#         self._history = []
#         self._func = func
#
#     def save(self, *args, **kwargs):
#         input_text = args
#         output_text = self._func(*args, **kwargs)
#         shift = kwargs.get("shift")
#         operation_name = self.__str__()
#         operation = {
#             "name": operation_name,
#             "input_text": input_text,
#             "output_text": output_text,
#             "shift": shift,
#             "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#         }
#         self._history.append(operation)
#
#     @property
#     def call_history(self):
#         return self._history
#
#         def operation_logger(func):
#             def wrapper_func(*args, **kwargs):
#                 input_text = args[0]
#                 output_text = func(*args, **kwargs)
#                 shift = kwargs.get("shift")
#                 operation = {
#                     "name":operation_name,
#                     "input_text": input_text,
#                     "output_text": output_text,
#                     "shift": shift,
#                     "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#                 }
#
#                 return output_text
#             return wrapper_func
#
#         return operation_logger
