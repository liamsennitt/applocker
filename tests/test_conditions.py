from unittest import TestCase
from applocker.conditions import (
    BinaryVersionRange,
    FilePublisherCondition,
    FilePathCondition,
    FileHash,
    FileHashCondition,
)


class TestBinaryVersionRange(TestCase):
    def test_default_low_section(self):
        binary_version_range = BinaryVersionRange()
        self.assertEqual(binary_version_range.low_section, "*")

    def test_valid_low_section(self):
        binary_version_range = BinaryVersionRange(low_section="0.0.0.0")
        self.assertEqual(binary_version_range.low_section, "0.0.0.0")

    def test_invalid_low_section_type(self):
        with self.assertRaises(TypeError):
            BinaryVersionRange(low_section=False)

    def test_default_high_section(self):
        binary_version_range = BinaryVersionRange()
        self.assertEqual(binary_version_range.high_section, "*")

    def test_valid_high_section(self):
        binary_version_range = BinaryVersionRange(high_section="0.0.0.0")
        self.assertEqual(binary_version_range.high_section, "0.0.0.0")

    def test_invalid_high_section_type(self):
        with self.assertRaises(TypeError):
            BinaryVersionRange(high_section=False)


class TestFilePublisherCondition(TestCase):
    def test_default_publisher_name(self):
        condition = FilePublisherCondition()
        self.assertEqual(condition.publisher_name, "*")

    def test_valid_publisher_name(self):
        condition = FilePublisherCondition(publisher_name="publisher_name")
        self.assertEqual(condition.publisher_name, "publisher_name")

    def test_invalid_publisher_name_type(self):
        with self.assertRaises(TypeError):
            FilePublisherCondition(publisher_name=False)

    def test_default_product_name(self):
        condition = FilePublisherCondition()
        self.assertEqual(condition.product_name, "*")

    def test_valid_product_name(self):
        condition = FilePublisherCondition(product_name="product_name")
        self.assertEqual(condition.product_name, "product_name")

    def test_invalid_product_name_type(self):
        with self.assertRaises(TypeError):
            FilePublisherCondition(product_name=False)

    def test_default_binary_name(self):
        condition = FilePublisherCondition()
        self.assertEqual(condition.binary_name, "*")

    def test_valid_binary_name(self):
        condition = FilePublisherCondition(binary_name="binary_name")
        self.assertEqual(condition.binary_name, "binary_name")

    def test_invalid_binary_name_type(self):
        with self.assertRaises(TypeError):
            FilePublisherCondition(binary_name=False)


class TestFilePathCondition(TestCase):
    def test_default_path(self):
        condition = FilePathCondition()
        self.assertEqual(condition.path, "*")

    def test_valid_path(self):
        condition = FilePathCondition(path="path")
        self.assertEqual(condition.path, "path")

    def test_invalid_path_type(self):
        with self.assertRaises(TypeError):
            FilePathCondition(path=False)


class TestFileHash(TestCase):
    def test_valid(self):
        file_hash = FileHash(
            type="", data="", source_file_name="", source_file_length=""
        )
        self.assertIsInstance(file_hash, FileHash)

    def test_invalid_type_type(self):
        with self.assertRaises(TypeError):
            FileHash(type=False, data="", source_file_name="", source_file_length="")

    def test_invalid_data_type(self):
        with self.assertRaises(TypeError):
            FileHash(type="", data=False, source_file_name="", source_file_length="")

    def test_invalid_source_file_name_type(self):
        with self.assertRaises(TypeError):
            FileHash(type="", data="", source_file_name=False, source_file_length="")

    def test_invalid_source_file_length_type(self):
        with self.assertRaises(TypeError):
            FileHash(type="", data="", source_file_name="", source_file_length=False)


class TestFileHashCondition(TestCase):
    def test_default_file_hashes(self):
        condition = FileHashCondition()
        self.assertEqual(condition.file_hashes, [])

    def test_valid_file_hashes(self):
        condition = FileHashCondition(file_hashes=[])
        self.assertIsInstance(condition, FileHashCondition)

    def test_invalid_file_hashes_type(self):
        with self.assertRaises(TypeError):
            FileHashCondition(file_hashes=False)

    def test_valid_file_hashes_element(self):
        file_hash = FileHash(
            type="", data="", source_file_name="", source_file_length=""
        )
        condition = FileHashCondition(file_hashes=[file_hash])
        self.assertIsInstance(condition, FileHashCondition)

    def test_invalid_file_hashes_element_type(self):
        with self.assertRaises(TypeError):
            FileHashCondition(file_hashes=[False])
