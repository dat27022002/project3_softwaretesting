import unittest

# Khởi tạo TestLoader
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# Thêm các test vào TestSuite
suite.addTests(loader.discover('./grading_feedback'))


# Khởi tạo TestRunner và chạy TestSuite
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)