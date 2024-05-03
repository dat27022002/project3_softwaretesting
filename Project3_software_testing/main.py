import unittest

# Khởi tạo TestLoader
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# Thêm các test vào TestSuite
suite.addTests(loader.discover('./test_requirement1'))


# Khởi tạo TestRunner và chạy TestSuite
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)