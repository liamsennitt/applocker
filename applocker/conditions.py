from xml.etree.ElementTree import Element


class BinaryVersionRange(Element):
    def __init__(self, *, low_section="*", high_section="*"):
        super(BinaryVersionRange, self).__init__("BinaryVersionRange")
        self.low_section = low_section
        self.high_section = high_section

    @property
    def low_section(self):
        return self.get("LowSection")

    @low_section.setter
    def low_section(self, low_section):
        if isinstance(low_section, str):
            self.set("LowSection", low_section)
        else:
            raise TypeError(f"invalid type for low_section: {type(low_section)}")

    @property
    def high_section(self):
        return self.get("HighSection")

    @high_section.setter
    def high_section(self, high_section):
        if isinstance(high_section, str):
            self.set("HighSection", high_section)
        else:
            raise TypeError(f"invalid type for high_section: {type(high_section)}")

    @classmethod
    def from_element(cls, element):
        return cls(
            low_section=element.get("LowSection"),
            high_section=element.get("HighSection"),
        )


class FilePublisherCondition(Element):
    def __init__(
        self,
        *,
        publisher_name="*",
        product_name="*",
        binary_name="*",
        binary_version_range=BinaryVersionRange(),
    ):
        super(FilePublisherCondition, self).__init__("FilePublisherCondition")
        self.publisher_name = publisher_name
        self.product_name = product_name
        self.binary_name = binary_name
        self.binary_version_range = binary_version_range

    @property
    def publisher_name(self):
        return self.get("PublisherName")

    @publisher_name.setter
    def publisher_name(self, publisher_name):
        if isinstance(publisher_name, str):
            self.set("PublisherName", publisher_name)
        else:
            raise TypeError(f"invalid type for publisher_name: {type(publisher_name)}")

    @property
    def product_name(self):
        return self.get("ProductName")

    @product_name.setter
    def product_name(self, product_name):
        if isinstance(product_name, str):
            self.set("ProductName", product_name)
        else:
            raise TypeError(f"invalid type for product_name: {type(product_name)}")

    @property
    def binary_name(self):
        return self.get("BinaryName")

    @binary_name.setter
    def binary_name(self, binary_name):
        if isinstance(binary_name, str):
            self.set("BinaryName", binary_name)
        else:
            raise TypeError(f"invalid type for binary_name: {type(binary_name)}")

    @property
    def binary_version_range(self):
        return self.find("BinaryVersionRange")

    @binary_version_range.setter
    def binary_version_range(self, binary_version_range):
        if isinstance(binary_version_range, BinaryVersionRange):
            self.append(binary_version_range)
        elif isinstance(binary_version_range, Element):
            self.append(BinaryVersionRange.from_element(binary_version_range))
        else:
            raise TypeError(
                f"invalid type for binary_version_range: {type(binary_version_range)}"
            )

    @classmethod
    def from_element(cls, element):
        return cls(
            publisher_name=element.get("PublisherName"),
            product_name=element.get("ProductName"),
            binary_name=element.get("BinaryName"),
            binary_version_range=element.find("BinaryVersionRange"),
        )


class FilePathCondition(Element):
    def __init__(self, *, path="*"):
        super(FilePathCondition, self).__init__("FilePathCondition")
        self.path = path

    @property
    def path(self):
        return self.get("Path")

    @path.setter
    def path(self, path):
        if isinstance(path, str):
            self.set("Path", path)
        else:
            raise TypeError(f"invalid type for path: {type(path)}")

    @classmethod
    def from_element(cls, element):
        return cls(path=element.get("Path"))


class FileHash(Element):
    def __init__(self, *, type, data, source_file_name, source_file_length):
        super(FileHash, self).__init__("FileHash")
        self.type = type
        self.data = data
        self.source_file_name = source_file_name
        self.source_file_length = source_file_length

    @property
    def type(self):
        return self.get("Type")

    @type.setter
    def type(self, type):
        if isinstance(type, str):
            self.set("Type", type)
        else:
            raise TypeError(f"invalid type for type: {type(type)}")

    @property
    def data(self):
        return self.get("Data")

    @data.setter
    def data(self, data):
        if isinstance(data, str):
            self.set("Data", data)
        else:
            raise TypeError(f"invalid type for data: {type(data)}")

    @property
    def source_file_name(self):
        return self.get("SourceFileName")

    @source_file_name.setter
    def source_file_name(self, source_file_name):
        if isinstance(source_file_name, str):
            self.set("SourceFileName", source_file_name)
        else:
            raise TypeError(
                f"invalid type for source_file_name: {type(source_file_name)}"
            )

    @property
    def source_file_length(self):
        return self.get("SourceFileLength")

    @source_file_length.setter
    def source_file_length(self, source_file_length):
        if isinstance(source_file_length, str):
            self.set("SourceFileLength", source_file_length)
        else:
            raise TypeError(
                f"invalid type for source_file_length: {type(source_file_length)}"
            )

    @classmethod
    def from_element(cls, element):
        return cls(
            type=element.get("Type"),
            data=element.get("Data"),
            source_file_name=element.get("SourceFileName"),
            source_file_length=element.get("SourceFileLength"),
        )


class FileHashCondition(Element):
    def __init__(self, file_hashes=[]):
        super(FileHashCondition, self).__init__("FileHashCondition")
        self.file_hashes = file_hashes

    @property
    def file_hashes(self):
        return self.findall("FileHash")

    @file_hashes.setter
    def file_hashes(self, file_hashes):
        if isinstance(file_hashes, list):
            for file_hash in file_hashes:
                if isinstance(file_hash, FileHash):
                    self.append(file_hash)
                elif isinstance(file_hash, Element):
                    self.append(FileHash.from_element(file_hash))
                else:
                    raise TypeError(
                        f"invalid type for file_hashes element: {type(file_hash)}"
                    )
        else:
            raise TypeError(f"invalid type for file_hashes: {type(file_hashes)}")

    @classmethod
    def from_element(cls, element):
        return cls(file_hashes=element.findall("FileHash"))
