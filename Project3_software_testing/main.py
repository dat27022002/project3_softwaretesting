import unittest
import sys

sys.path.append('./editcourse')
# Khởi tạo TestLoader
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# Thêm các test vào TestSuite
#suite.addTests(loader.discover('../Project3_software_testing'))
#suite.addTests(loader.discover('./login'))
#suite.addTests(loader.discover('./edit_course'))
suite.addTests(loader.discover('./search_student'))




# Khởi tạo TestRunner và chạy TestSuite
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)


