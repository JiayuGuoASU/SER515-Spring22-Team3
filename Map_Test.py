import unittest
import Map
# This calss tested if the Map class works
class Testing(unittest.TestCase):

    map = Map.Map(7, 4)
    
    def test_constructor(self):
        self.assertEqual(self.map.size, 7)
        self.assertEqual(self.map.density, 4)

    def test_writeLinks(self):
        self.assertEqual(self.map.link_str, "")
        self.assertEqual(self.map.link_str2, "")

        self.map.writeLinks()

        self.assertNotEqual(self.map.link_str, "")
        self.assertNotEqual(self.map.link_str2, "")

if __name__ == '__main__':
    unittest.main()
