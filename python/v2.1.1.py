from enum import Enum
from typing import Any, List, Optional, TypeVar, Type, Callable, cast
from datetime import datetime
import dateutil.parser


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


class AuthMethod(Enum):
    AUTH_REQUEST = "AUTH_REQUEST"
    WHITELIST = "WHITELIST"


class DimensionType(Enum):
    ENERGY = "ENERGY"
    FLAT = "FLAT"
    MAX_CURRENT = "MAX_CURRENT"
    MIN_CURRENT = "MIN_CURRENT"
    PARKING_TIME = "PARKING_TIME"
    TIME = "TIME"


class Dimension:
    type: DimensionType
    volume: float

    def __init__(self, type: DimensionType, volume: float) -> None:
        self.type = type
        self.volume = volume

    @staticmethod
    def from_dict(obj: Any) -> 'Dimension':
        assert isinstance(obj, dict)
        type = DimensionType(obj.get("type"))
        volume = from_float(obj.get("volume"))
        return Dimension(type, volume)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = to_enum(DimensionType, self.type)
        result["volume"] = to_float(self.volume)
        return result


class ChargingPeriod:
    dimensions: List[Dimension]
    start_date_time: str

    def __init__(self, dimensions: List[Dimension], start_date_time: str) -> None:
        self.dimensions = dimensions
        self.start_date_time = start_date_time

    @staticmethod
    def from_dict(obj: Any) -> 'ChargingPeriod':
        assert isinstance(obj, dict)
        dimensions = from_list(Dimension.from_dict, obj.get("dimensions"))
        start_date_time = from_str(obj.get("start_date_time"))
        return ChargingPeriod(dimensions, start_date_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["dimensions"] = from_list(lambda x: to_class(Dimension, x), self.dimensions)
        result["start_date_time"] = from_str(self.start_date_time)
        return result


class GeoLocation:
    latitude: Optional[str]
    longitude: Optional[str]

    def __init__(self, latitude: Optional[str], longitude: Optional[str]) -> None:
        self.latitude = latitude
        self.longitude = longitude

    @staticmethod
    def from_dict(obj: Any) -> 'GeoLocation':
        assert isinstance(obj, dict)
        latitude = from_union([from_str, from_none], obj.get("latitude"))
        longitude = from_union([from_str, from_none], obj.get("longitude"))
        return GeoLocation(latitude, longitude)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.latitude is not None:
            result["latitude"] = from_union([from_str, from_none], self.latitude)
        if self.longitude is not None:
            result["longitude"] = from_union([from_str, from_none], self.longitude)
        return result


class DisplayText:
    language: str
    text: str

    def __init__(self, language: str, text: str) -> None:
        self.language = language
        self.text = text

    @staticmethod
    def from_dict(obj: Any) -> 'DisplayText':
        assert isinstance(obj, dict)
        language = from_str(obj.get("language"))
        text = from_str(obj.get("text"))
        return DisplayText(language, text)

    def to_dict(self) -> dict:
        result: dict = {}
        result["language"] = from_str(self.language)
        result["text"] = from_str(self.text)
        return result


class EnergySourceSource(Enum):
    COAL = "COAL"
    GAS = "GAS"
    GENERAL_FOSSIL = "GENERAL_FOSSIL"
    GENERAL_GREEN = "GENERAL_GREEN"
    NUCLEAR = "NUCLEAR"
    SOLAR = "SOLAR"
    WATER = "WATER"
    WIND = "WIND"


class EnergySource:
    percentage: float
    source: EnergySourceSource

    def __init__(self, percentage: float, source: EnergySourceSource) -> None:
        self.percentage = percentage
        self.source = source

    @staticmethod
    def from_dict(obj: Any) -> 'EnergySource':
        assert isinstance(obj, dict)
        percentage = from_float(obj.get("percentage"))
        source = EnergySourceSource(obj.get("source"))
        return EnergySource(percentage, source)

    def to_dict(self) -> dict:
        result: dict = {}
        result["percentage"] = to_float(self.percentage)
        result["source"] = to_enum(EnergySourceSource, self.source)
        return result


class EnvironImpactSource(Enum):
    CARBON_DIOXIDE = "CARBON_DIOXIDE"
    NUCLEAR_WASTE = "NUCLEAR_WASTE"


class EnvironImpact:
    amount: float
    source: EnvironImpactSource

    def __init__(self, amount: float, source: EnvironImpactSource) -> None:
        self.amount = amount
        self.source = source

    @staticmethod
    def from_dict(obj: Any) -> 'EnvironImpact':
        assert isinstance(obj, dict)
        amount = from_float(obj.get("amount"))
        source = EnvironImpactSource(obj.get("source"))
        return EnvironImpact(amount, source)

    def to_dict(self) -> dict:
        result: dict = {}
        result["amount"] = to_float(self.amount)
        result["source"] = to_enum(EnvironImpactSource, self.source)
        return result


class EnergyMix:
    energy_product_name: Optional[str]
    energy_sources: Optional[List[EnergySource]]
    environ_impact: Optional[List[EnvironImpact]]
    is_green_energy: bool
    supplier_name: Optional[str]

    def __init__(self, energy_product_name: Optional[str], energy_sources: Optional[List[EnergySource]], environ_impact: Optional[List[EnvironImpact]], is_green_energy: bool, supplier_name: Optional[str]) -> None:
        self.energy_product_name = energy_product_name
        self.energy_sources = energy_sources
        self.environ_impact = environ_impact
        self.is_green_energy = is_green_energy
        self.supplier_name = supplier_name

    @staticmethod
    def from_dict(obj: Any) -> 'EnergyMix':
        assert isinstance(obj, dict)
        energy_product_name = from_union([from_none, from_str], obj.get("energy_product_name"))
        energy_sources = from_union([from_none, lambda x: from_list(EnergySource.from_dict, x)], obj.get("energy_sources"))
        environ_impact = from_union([from_none, lambda x: from_list(EnvironImpact.from_dict, x)], obj.get("environ_impact"))
        is_green_energy = from_bool(obj.get("is_green_energy"))
        supplier_name = from_union([from_none, from_str], obj.get("supplier_name"))
        return EnergyMix(energy_product_name, energy_sources, environ_impact, is_green_energy, supplier_name)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.energy_product_name is not None:
            result["energy_product_name"] = from_union([from_none, from_str], self.energy_product_name)
        if self.energy_sources is not None:
            result["energy_sources"] = from_union([from_none, lambda x: from_list(lambda x: to_class(EnergySource, x), x)], self.energy_sources)
        if self.environ_impact is not None:
            result["environ_impact"] = from_union([from_none, lambda x: from_list(lambda x: to_class(EnvironImpact, x), x)], self.environ_impact)
        result["is_green_energy"] = from_bool(self.is_green_energy)
        if self.supplier_name is not None:
            result["supplier_name"] = from_union([from_none, from_str], self.supplier_name)
        return result


class Capability(Enum):
    CHARGING_PROFILE_CAPABLE = "CHARGING_PROFILE_CAPABLE"
    CREDIT_CARD_PAYABLE = "CREDIT_CARD_PAYABLE"
    REMOTE_START_STOP_CAPABLE = "REMOTE_START_STOP_CAPABLE"
    RESERVABLE = "RESERVABLE"
    RFID_READER = "RFID_READER"
    UNLOCK_CAPABLE = "UNLOCK_CAPABLE"


class Format(Enum):
    CABLE = "CABLE"
    SOCKET = "SOCKET"


class PowerType(Enum):
    AC_1__PHASE = "AC_1_PHASE"
    AC_3__PHASE = "AC_3_PHASE"
    DC = "DC"


class Standard(Enum):
    CHADEMO = "CHADEMO"
    DOMESTIC_A = "DOMESTIC_A"
    DOMESTIC_B = "DOMESTIC_B"
    DOMESTIC_C = "DOMESTIC_C"
    DOMESTIC_D = "DOMESTIC_D"
    DOMESTIC_E = "DOMESTIC_E"
    DOMESTIC_F = "DOMESTIC_F"
    DOMESTIC_G = "DOMESTIC_G"
    DOMESTIC_H = "DOMESTIC_H"
    DOMESTIC_I = "DOMESTIC_I"
    DOMESTIC_J = "DOMESTIC_J"
    DOMESTIC_K = "DOMESTIC_K"
    DOMESTIC_L = "DOMESTIC_L"
    IEC_60309_2__SINGLE_16 = "IEC_60309_2_single_16"
    IEC_60309_2__THREE_16 = "IEC_60309_2_three_16"
    IEC_60309_2__THREE_32 = "IEC_60309_2_three_32"
    IEC_60309_2__THREE_64 = "IEC_60309_2_three_64"
    IEC_62196__T1 = "IEC_62196_T1"
    IEC_62196__T1_COMBO = "IEC_62196_T1_COMBO"
    IEC_62196__T2 = "IEC_62196_T2"
    IEC_62196__T2_COMBO = "IEC_62196_T2_COMBO"
    IEC_62196__T3_A = "IEC_62196_T3A"
    IEC_62196__T3_C = "IEC_62196_T3C"
    TESLA_R = "TESLA_R"
    TESLA_S = "TESLA_S"


class Connector:
    amperage: Optional[int]
    format: Optional[Format]
    id: Optional[str]
    last_updated: Optional[str]
    power_type: Optional[PowerType]
    standard: Optional[Standard]
    tariff_id: Optional[str]
    terms_and_conditions: Optional[str]
    voltage: Optional[int]

    def __init__(self, amperage: Optional[int], format: Optional[Format], id: Optional[str], last_updated: Optional[str], power_type: Optional[PowerType], standard: Optional[Standard], tariff_id: Optional[str], terms_and_conditions: Optional[str], voltage: Optional[int]) -> None:
        self.amperage = amperage
        self.format = format
        self.id = id
        self.last_updated = last_updated
        self.power_type = power_type
        self.standard = standard
        self.tariff_id = tariff_id
        self.terms_and_conditions = terms_and_conditions
        self.voltage = voltage

    @staticmethod
    def from_dict(obj: Any) -> 'Connector':
        assert isinstance(obj, dict)
        amperage = from_union([from_int, from_none], obj.get("amperage"))
        format = from_union([Format, from_none], obj.get("format"))
        id = from_union([from_str, from_none], obj.get("id"))
        last_updated = from_union([from_str, from_none], obj.get("last_updated"))
        power_type = from_union([PowerType, from_none], obj.get("power_type"))
        standard = from_union([Standard, from_none], obj.get("standard"))
        tariff_id = from_union([from_none, from_str], obj.get("tariff_id"))
        terms_and_conditions = from_union([from_none, from_str], obj.get("terms_and_conditions"))
        voltage = from_union([from_int, from_none], obj.get("voltage"))
        return Connector(amperage, format, id, last_updated, power_type, standard, tariff_id, terms_and_conditions, voltage)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.amperage is not None:
            result["amperage"] = from_union([from_int, from_none], self.amperage)
        if self.format is not None:
            result["format"] = from_union([lambda x: to_enum(Format, x), from_none], self.format)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.last_updated is not None:
            result["last_updated"] = from_union([from_str, from_none], self.last_updated)
        if self.power_type is not None:
            result["power_type"] = from_union([lambda x: to_enum(PowerType, x), from_none], self.power_type)
        if self.standard is not None:
            result["standard"] = from_union([lambda x: to_enum(Standard, x), from_none], self.standard)
        if self.tariff_id is not None:
            result["tariff_id"] = from_union([from_none, from_str], self.tariff_id)
        if self.terms_and_conditions is not None:
            result["terms_and_conditions"] = from_union([from_none, from_str], self.terms_and_conditions)
        if self.voltage is not None:
            result["voltage"] = from_union([from_int, from_none], self.voltage)
        return result


class Category(Enum):
    CHARGER = "CHARGER"
    ENTRANCE = "ENTRANCE"
    LOCATION = "LOCATION"
    NETWORK = "NETWORK"
    OPERATOR = "OPERATOR"
    OTHER = "OTHER"
    OWNER = "OWNER"


class Image:
    category: Category
    height: Optional[int]
    thumbnail: Optional[str]
    type: str
    url: str
    width: Optional[int]

    def __init__(self, category: Category, height: Optional[int], thumbnail: Optional[str], type: str, url: str, width: Optional[int]) -> None:
        self.category = category
        self.height = height
        self.thumbnail = thumbnail
        self.type = type
        self.url = url
        self.width = width

    @staticmethod
    def from_dict(obj: Any) -> 'Image':
        assert isinstance(obj, dict)
        category = Category(obj.get("category"))
        height = from_union([from_int, from_none], obj.get("height"))
        thumbnail = from_union([from_none, from_str], obj.get("thumbnail"))
        type = from_str(obj.get("type"))
        url = from_str(obj.get("url"))
        width = from_union([from_int, from_none], obj.get("width"))
        return Image(category, height, thumbnail, type, url, width)

    def to_dict(self) -> dict:
        result: dict = {}
        result["category"] = to_enum(Category, self.category)
        if self.height is not None:
            result["height"] = from_union([from_int, from_none], self.height)
        if self.thumbnail is not None:
            result["thumbnail"] = from_union([from_none, from_str], self.thumbnail)
        result["type"] = from_str(self.type)
        result["url"] = from_str(self.url)
        if self.width is not None:
            result["width"] = from_union([from_int, from_none], self.width)
        return result


class ParkingRestriction(Enum):
    CUSTOMERS = "CUSTOMERS"
    DISABLED = "DISABLED"
    EV_ONLY = "EV_ONLY"
    MOTORCYCLES = "MOTORCYCLES"
    PLUGGED = "PLUGGED"


class EvseStatus(Enum):
    AVAILABLE = "AVAILABLE"
    BLOCKED = "BLOCKED"
    CHARGING = "CHARGING"
    INOPERATIVE = "INOPERATIVE"
    OUTOFORDER = "OUTOFORDER"
    PLANNED = "PLANNED"
    REMOVED = "REMOVED"
    RESERVED = "RESERVED"
    UNKNOWN = "UNKNOWN"


class StatusSchedule:
    period_begin: str
    period_end: Optional[str]
    status: EvseStatus

    def __init__(self, period_begin: str, period_end: Optional[str], status: EvseStatus) -> None:
        self.period_begin = period_begin
        self.period_end = period_end
        self.status = status

    @staticmethod
    def from_dict(obj: Any) -> 'StatusSchedule':
        assert isinstance(obj, dict)
        period_begin = from_str(obj.get("period_begin"))
        period_end = from_union([from_str, from_none], obj.get("period_end"))
        status = EvseStatus(obj.get("status"))
        return StatusSchedule(period_begin, period_end, status)

    def to_dict(self) -> dict:
        result: dict = {}
        result["period_begin"] = from_str(self.period_begin)
        if self.period_end is not None:
            result["period_end"] = from_union([from_str, from_none], self.period_end)
        result["status"] = to_enum(EvseStatus, self.status)
        return result


class Evse:
    capabilities: Optional[List[Capability]]
    connectors: Optional[List[Connector]]
    coordinates: Optional[GeoLocation]
    directions: Optional[List[DisplayText]]
    evse_id: Optional[str]
    floor_level: Optional[str]
    images: Optional[List[Image]]
    last_updated: Optional[str]
    parking_restrictions: Optional[List[ParkingRestriction]]
    physical_reference: Optional[str]
    status: Optional[EvseStatus]
    status_schedule: Optional[List[StatusSchedule]]
    uid: Optional[str]

    def __init__(self, capabilities: Optional[List[Capability]], connectors: Optional[List[Connector]], coordinates: Optional[GeoLocation], directions: Optional[List[DisplayText]], evse_id: Optional[str], floor_level: Optional[str], images: Optional[List[Image]], last_updated: Optional[str], parking_restrictions: Optional[List[ParkingRestriction]], physical_reference: Optional[str], status: Optional[EvseStatus], status_schedule: Optional[List[StatusSchedule]], uid: Optional[str]) -> None:
        self.capabilities = capabilities
        self.connectors = connectors
        self.coordinates = coordinates
        self.directions = directions
        self.evse_id = evse_id
        self.floor_level = floor_level
        self.images = images
        self.last_updated = last_updated
        self.parking_restrictions = parking_restrictions
        self.physical_reference = physical_reference
        self.status = status
        self.status_schedule = status_schedule
        self.uid = uid

    @staticmethod
    def from_dict(obj: Any) -> 'Evse':
        assert isinstance(obj, dict)
        capabilities = from_union([from_none, lambda x: from_list(Capability, x)], obj.get("capabilities"))
        connectors = from_union([lambda x: from_list(Connector.from_dict, x), from_none], obj.get("connectors"))
        coordinates = from_union([from_none, GeoLocation.from_dict], obj.get("coordinates"))
        directions = from_union([from_none, lambda x: from_list(DisplayText.from_dict, x)], obj.get("directions"))
        evse_id = from_union([from_none, from_str], obj.get("evse_id"))
        floor_level = from_union([from_none, from_str], obj.get("floor_level"))
        images = from_union([from_none, lambda x: from_list(Image.from_dict, x)], obj.get("images"))
        last_updated = from_union([from_str, from_none], obj.get("last_updated"))
        parking_restrictions = from_union([from_none, lambda x: from_list(ParkingRestriction, x)], obj.get("parking_restrictions"))
        physical_reference = from_union([from_none, from_str], obj.get("physical_reference"))
        status = from_union([EvseStatus, from_none], obj.get("status"))
        status_schedule = from_union([from_none, lambda x: from_list(StatusSchedule.from_dict, x)], obj.get("status_schedule"))
        uid = from_union([from_str, from_none], obj.get("uid"))
        return Evse(capabilities, connectors, coordinates, directions, evse_id, floor_level, images, last_updated, parking_restrictions, physical_reference, status, status_schedule, uid)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.capabilities is not None:
            result["capabilities"] = from_union([from_none, lambda x: from_list(lambda x: to_enum(Capability, x), x)], self.capabilities)
        if self.connectors is not None:
            result["connectors"] = from_union([lambda x: from_list(lambda x: to_class(Connector, x), x), from_none], self.connectors)
        if self.coordinates is not None:
            result["coordinates"] = from_union([from_none, lambda x: to_class(GeoLocation, x)], self.coordinates)
        if self.directions is not None:
            result["directions"] = from_union([from_none, lambda x: from_list(lambda x: to_class(DisplayText, x), x)], self.directions)
        if self.evse_id is not None:
            result["evse_id"] = from_union([from_none, from_str], self.evse_id)
        if self.floor_level is not None:
            result["floor_level"] = from_union([from_none, from_str], self.floor_level)
        if self.images is not None:
            result["images"] = from_union([from_none, lambda x: from_list(lambda x: to_class(Image, x), x)], self.images)
        if self.last_updated is not None:
            result["last_updated"] = from_union([from_str, from_none], self.last_updated)
        if self.parking_restrictions is not None:
            result["parking_restrictions"] = from_union([from_none, lambda x: from_list(lambda x: to_enum(ParkingRestriction, x), x)], self.parking_restrictions)
        if self.physical_reference is not None:
            result["physical_reference"] = from_union([from_none, from_str], self.physical_reference)
        if self.status is not None:
            result["status"] = from_union([lambda x: to_enum(EvseStatus, x), from_none], self.status)
        if self.status_schedule is not None:
            result["status_schedule"] = from_union([from_none, lambda x: from_list(lambda x: to_class(StatusSchedule, x), x)], self.status_schedule)
        if self.uid is not None:
            result["uid"] = from_union([from_str, from_none], self.uid)
        return result


class Facility(Enum):
    AIRPORT = "AIRPORT"
    BUS_STOP = "BUS_STOP"
    CAFE = "CAFE"
    CARPOOL_PARKING = "CARPOOL_PARKING"
    FUEL_STATION = "FUEL_STATION"
    HOTEL = "HOTEL"
    MALL = "MALL"
    MUSEUM = "MUSEUM"
    NATURE = "NATURE"
    RECREATION_AREA = "RECREATION_AREA"
    RESTAURANT = "RESTAURANT"
    SPORT = "SPORT"
    SUPERMARKET = "SUPERMARKET"
    TAXI_STAND = "TAXI_STAND"
    TRAIN_STATION = "TRAIN_STATION"
    WIFI = "WIFI"


class ExceptionalPeriod:
    period_begin: str
    period_end: str

    def __init__(self, period_begin: str, period_end: str) -> None:
        self.period_begin = period_begin
        self.period_end = period_end

    @staticmethod
    def from_dict(obj: Any) -> 'ExceptionalPeriod':
        assert isinstance(obj, dict)
        period_begin = from_str(obj.get("period_begin"))
        period_end = from_str(obj.get("period_end"))
        return ExceptionalPeriod(period_begin, period_end)

    def to_dict(self) -> dict:
        result: dict = {}
        result["period_begin"] = from_str(self.period_begin)
        result["period_end"] = from_str(self.period_end)
        return result


class RegularHours:
    period_begin: Optional[str]
    period_end: Optional[str]
    weekday: Optional[int]

    def __init__(self, period_begin: Optional[str], period_end: Optional[str], weekday: Optional[int]) -> None:
        self.period_begin = period_begin
        self.period_end = period_end
        self.weekday = weekday

    @staticmethod
    def from_dict(obj: Any) -> 'RegularHours':
        assert isinstance(obj, dict)
        period_begin = from_union([from_str, from_none], obj.get("period_begin"))
        period_end = from_union([from_str, from_none], obj.get("period_end"))
        weekday = from_union([from_int, from_none], obj.get("weekday"))
        return RegularHours(period_begin, period_end, weekday)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.period_begin is not None:
            result["period_begin"] = from_union([from_str, from_none], self.period_begin)
        if self.period_end is not None:
            result["period_end"] = from_union([from_str, from_none], self.period_end)
        if self.weekday is not None:
            result["weekday"] = from_union([from_int, from_none], self.weekday)
        return result


class Hours:
    exceptional_closings: Optional[List[ExceptionalPeriod]]
    exceptional_openings: Optional[List[ExceptionalPeriod]]
    regular_hours: Optional[List[RegularHours]]
    twentyfourseven: Optional[bool]

    def __init__(self, exceptional_closings: Optional[List[ExceptionalPeriod]], exceptional_openings: Optional[List[ExceptionalPeriod]], regular_hours: Optional[List[RegularHours]], twentyfourseven: Optional[bool]) -> None:
        self.exceptional_closings = exceptional_closings
        self.exceptional_openings = exceptional_openings
        self.regular_hours = regular_hours
        self.twentyfourseven = twentyfourseven

    @staticmethod
    def from_dict(obj: Any) -> 'Hours':
        assert isinstance(obj, dict)
        exceptional_closings = from_union([from_none, lambda x: from_list(ExceptionalPeriod.from_dict, x)], obj.get("exceptional_closings"))
        exceptional_openings = from_union([from_none, lambda x: from_list(ExceptionalPeriod.from_dict, x)], obj.get("exceptional_openings"))
        regular_hours = from_union([from_none, lambda x: from_list(RegularHours.from_dict, x)], obj.get("regular_hours"))
        twentyfourseven = from_union([from_none, from_bool], obj.get("twentyfourseven"))
        return Hours(exceptional_closings, exceptional_openings, regular_hours, twentyfourseven)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.exceptional_closings is not None:
            result["exceptional_closings"] = from_union([from_none, lambda x: from_list(lambda x: to_class(ExceptionalPeriod, x), x)], self.exceptional_closings)
        if self.exceptional_openings is not None:
            result["exceptional_openings"] = from_union([from_none, lambda x: from_list(lambda x: to_class(ExceptionalPeriod, x), x)], self.exceptional_openings)
        if self.regular_hours is not None:
            result["regular_hours"] = from_union([from_none, lambda x: from_list(lambda x: to_class(RegularHours, x), x)], self.regular_hours)
        if self.twentyfourseven is not None:
            result["twentyfourseven"] = from_union([from_none, from_bool], self.twentyfourseven)
        return result


class BusinessDetails:
    logo: Optional[Image]
    name: str
    website: Optional[str]

    def __init__(self, logo: Optional[Image], name: str, website: Optional[str]) -> None:
        self.logo = logo
        self.name = name
        self.website = website

    @staticmethod
    def from_dict(obj: Any) -> 'BusinessDetails':
        assert isinstance(obj, dict)
        logo = from_union([from_none, Image.from_dict], obj.get("logo"))
        name = from_str(obj.get("name"))
        website = from_union([from_none, from_str], obj.get("website"))
        return BusinessDetails(logo, name, website)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.logo is not None:
            result["logo"] = from_union([from_none, lambda x: to_class(Image, x)], self.logo)
        result["name"] = from_str(self.name)
        if self.website is not None:
            result["website"] = from_union([from_none, from_str], self.website)
        return result


class RelatedLocation:
    latitude: Optional[str]
    longitude: Optional[str]
    name: Optional[DisplayText]

    def __init__(self, latitude: Optional[str], longitude: Optional[str], name: Optional[DisplayText]) -> None:
        self.latitude = latitude
        self.longitude = longitude
        self.name = name

    @staticmethod
    def from_dict(obj: Any) -> 'RelatedLocation':
        assert isinstance(obj, dict)
        latitude = from_union([from_str, from_none], obj.get("latitude"))
        longitude = from_union([from_str, from_none], obj.get("longitude"))
        name = from_union([DisplayText.from_dict, from_none], obj.get("name"))
        return RelatedLocation(latitude, longitude, name)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.latitude is not None:
            result["latitude"] = from_union([from_str, from_none], self.latitude)
        if self.longitude is not None:
            result["longitude"] = from_union([from_str, from_none], self.longitude)
        if self.name is not None:
            result["name"] = from_union([lambda x: to_class(DisplayText, x), from_none], self.name)
        return result


class LocationType(Enum):
    ON_STREET = "ON_STREET"
    OTHER = "OTHER"
    PARKING_GARAGE = "PARKING_GARAGE"
    PARKING_LOT = "PARKING_LOT"
    UNDERGROUND_GARAGE = "UNDERGROUND_GARAGE"
    UNKNOWN = "UNKNOWN"


class CdrLocation:
    id: str
    type: LocationType
    address: str
    city: str
    postal_code: str
    country: str
    coordinates: GeoLocation
    last_updated: str
    charging_when_closed: Optional[bool]
    directions: Optional[List[DisplayText]]
    energy_mix: Optional[EnergyMix]
    evses: Optional[List[Evse]]
    facilities: Optional[List[Facility]]
    images: Optional[List[Image]]
    name: Optional[str]
    opening_times: Optional[Hours]
    operator: Optional[BusinessDetails]
    owner: Optional[BusinessDetails]
    related_locations: Optional[List[RelatedLocation]]
    suboperator: Optional[BusinessDetails]
    time_zone: Optional[str]

    def __init__(self, id: str, type: LocationType, address: str, city: str, postal_code: str, country: str, coordinates: GeoLocation, last_updated: str, charging_when_closed: Optional[bool], directions: Optional[List[DisplayText]], energy_mix: Optional[EnergyMix], evses: Optional[List[Evse]], facilities: Optional[List[Facility]], images: Optional[List[Image]], name: Optional[str], opening_times: Optional[Hours], operator: Optional[BusinessDetails], owner: Optional[BusinessDetails], related_locations: Optional[List[RelatedLocation]], suboperator: Optional[BusinessDetails], time_zone: Optional[str]) -> None:
        self.id = id
        self.type = type
        self.address = address
        self.city = city
        self.postal_code = postal_code
        self.country = country
        self.coordinates = coordinates
        self.last_updated = last_updated
        self.charging_when_closed = charging_when_closed
        self.directions = directions
        self.energy_mix = energy_mix
        self.evses = evses
        self.facilities = facilities
        self.images = images
        self.name = name
        self.opening_times = opening_times
        self.operator = operator
        self.owner = owner
        self.related_locations = related_locations
        self.suboperator = suboperator
        self.time_zone = time_zone

    @staticmethod
    def from_dict(obj: Any) -> 'CdrLocation':
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        type = LocationType(obj.get("type"))
        address = from_str(obj.get("address"))
        city = from_str(obj.get("city"))
        postal_code = from_str(obj.get("postal_code"))
        country = from_str(obj.get("country"))
        coordinates = GeoLocation.from_dict(obj.get("coordinates"))
        last_updated = from_str(obj.get("last_updated"))
        charging_when_closed = from_union([from_none, from_bool], obj.get("charging_when_closed"))
        directions = from_union([from_none, lambda x: from_list(DisplayText.from_dict, x)], obj.get("directions"))
        energy_mix = from_union([from_none, EnergyMix.from_dict], obj.get("energy_mix"))
        evses = from_union([from_none, lambda x: from_list(Evse.from_dict, x)], obj.get("evses"))
        facilities = from_union([from_none, lambda x: from_list(Facility, x)], obj.get("facilities"))
        images = from_union([from_none, lambda x: from_list(Image.from_dict, x)], obj.get("images"))
        name = from_union([from_none, from_str], obj.get("name"))
        opening_times = from_union([from_none, Hours.from_dict], obj.get("opening_times"))
        operator = from_union([from_none, BusinessDetails.from_dict], obj.get("operator"))
        owner = from_union([from_none, BusinessDetails.from_dict], obj.get("owner"))
        related_locations = from_union([from_none, lambda x: from_list(RelatedLocation.from_dict, x)], obj.get("related_locations"))
        suboperator = from_union([from_none, BusinessDetails.from_dict], obj.get("suboperator"))
        time_zone = from_union([from_none, from_str], obj.get("time_zone"))
        return CdrLocation(id, type, address, city, postal_code, country, coordinates, last_updated, charging_when_closed, directions, energy_mix, evses, facilities, images, name, opening_times, operator, owner, related_locations, suboperator, time_zone)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(self.id)
        result["type"] = to_enum(LocationType, self.type)
        result["address"] = from_str(self.address)
        result["city"] = from_str(self.city)
        result["postal_code"] = from_str(self.postal_code)
        result["country"] = from_str(self.country)
        result["coordinates"] = to_class(GeoLocation, self.coordinates)
        result["last_updated"] = from_str(self.last_updated)
        if self.charging_when_closed is not None:
            result["charging_when_closed"] = from_union([from_none, from_bool], self.charging_when_closed)
        if self.directions is not None:
            result["directions"] = from_union([from_none, lambda x: from_list(lambda x: to_class(DisplayText, x), x)], self.directions)
        if self.energy_mix is not None:
            result["energy_mix"] = from_union([from_none, lambda x: to_class(EnergyMix, x)], self.energy_mix)
        if self.evses is not None:
            result["evses"] = from_union([from_none, lambda x: from_list(lambda x: to_class(Evse, x), x)], self.evses)
        if self.facilities is not None:
            result["facilities"] = from_union([from_none, lambda x: from_list(lambda x: to_enum(Facility, x), x)], self.facilities)
        if self.images is not None:
            result["images"] = from_union([from_none, lambda x: from_list(lambda x: to_class(Image, x), x)], self.images)
        if self.name is not None:
            result["name"] = from_union([from_none, from_str], self.name)
        if self.opening_times is not None:
            result["opening_times"] = from_union([from_none, lambda x: to_class(Hours, x)], self.opening_times)
        if self.operator is not None:
            result["operator"] = from_union([from_none, lambda x: to_class(BusinessDetails, x)], self.operator)
        if self.owner is not None:
            result["owner"] = from_union([from_none, lambda x: to_class(BusinessDetails, x)], self.owner)
        if self.related_locations is not None:
            result["related_locations"] = from_union([from_none, lambda x: from_list(lambda x: to_class(RelatedLocation, x), x)], self.related_locations)
        if self.suboperator is not None:
            result["suboperator"] = from_union([from_none, lambda x: to_class(BusinessDetails, x)], self.suboperator)
        if self.time_zone is not None:
            result["time_zone"] = from_union([from_none, from_str], self.time_zone)
        return result


class PriceComponentType(Enum):
    ENERGY = "ENERGY"
    FLAT = "FLAT"
    PARKING_TIME = "PARKING_TIME"
    TIME = "TIME"


class PriceComponent:
    price: float
    step_size: int
    type: PriceComponentType

    def __init__(self, price: float, step_size: int, type: PriceComponentType) -> None:
        self.price = price
        self.step_size = step_size
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'PriceComponent':
        assert isinstance(obj, dict)
        price = from_float(obj.get("price"))
        step_size = from_int(obj.get("step_size"))
        type = PriceComponentType(obj.get("type"))
        return PriceComponent(price, step_size, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["price"] = to_float(self.price)
        result["step_size"] = from_int(self.step_size)
        result["type"] = to_enum(PriceComponentType, self.type)
        return result


class DayOfWeek(Enum):
    FRIDAY = "FRIDAY"
    MONDAY = "MONDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"
    THURSDAY = "THURSDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"


class Restrictions:
    day_of_week: Optional[List[DayOfWeek]]
    end_date: Optional[datetime]
    end_time: Optional[str]
    max_duration: Optional[int]
    max_kwh: Optional[float]
    max_power: Optional[float]
    min_duration: Optional[int]
    min_kwh: Optional[float]
    min_power: Optional[float]
    start_date: Optional[datetime]
    start_time: Optional[str]

    def __init__(self, day_of_week: Optional[List[DayOfWeek]], end_date: Optional[datetime], end_time: Optional[str], max_duration: Optional[int], max_kwh: Optional[float], max_power: Optional[float], min_duration: Optional[int], min_kwh: Optional[float], min_power: Optional[float], start_date: Optional[datetime], start_time: Optional[str]) -> None:
        self.day_of_week = day_of_week
        self.end_date = end_date
        self.end_time = end_time
        self.max_duration = max_duration
        self.max_kwh = max_kwh
        self.max_power = max_power
        self.min_duration = min_duration
        self.min_kwh = min_kwh
        self.min_power = min_power
        self.start_date = start_date
        self.start_time = start_time

    @staticmethod
    def from_dict(obj: Any) -> 'Restrictions':
        assert isinstance(obj, dict)
        day_of_week = from_union([from_none, lambda x: from_list(DayOfWeek, x)], obj.get("day_of_week"))
        end_date = from_union([from_none, from_datetime], obj.get("end_date"))
        end_time = from_union([from_none, from_str], obj.get("end_time"))
        max_duration = from_union([from_none, from_int], obj.get("max_duration"))
        max_kwh = from_union([from_none, from_float], obj.get("max_kwh"))
        max_power = from_union([from_none, from_float], obj.get("max_power"))
        min_duration = from_union([from_none, from_int], obj.get("min_duration"))
        min_kwh = from_union([from_none, from_float], obj.get("min_kwh"))
        min_power = from_union([from_none, from_float], obj.get("min_power"))
        start_date = from_union([from_none, from_datetime], obj.get("start_date"))
        start_time = from_union([from_none, from_str], obj.get("start_time"))
        return Restrictions(day_of_week, end_date, end_time, max_duration, max_kwh, max_power, min_duration, min_kwh, min_power, start_date, start_time)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.day_of_week is not None:
            result["day_of_week"] = from_union([from_none, lambda x: from_list(lambda x: to_enum(DayOfWeek, x), x)], self.day_of_week)
        if self.end_date is not None:
            result["end_date"] = from_union([from_none, lambda x: x.isoformat()], self.end_date)
        if self.end_time is not None:
            result["end_time"] = from_union([from_none, from_str], self.end_time)
        if self.max_duration is not None:
            result["max_duration"] = from_union([from_none, from_int], self.max_duration)
        if self.max_kwh is not None:
            result["max_kwh"] = from_union([from_none, to_float], self.max_kwh)
        if self.max_power is not None:
            result["max_power"] = from_union([from_none, to_float], self.max_power)
        if self.min_duration is not None:
            result["min_duration"] = from_union([from_none, from_int], self.min_duration)
        if self.min_kwh is not None:
            result["min_kwh"] = from_union([from_none, to_float], self.min_kwh)
        if self.min_power is not None:
            result["min_power"] = from_union([from_none, to_float], self.min_power)
        if self.start_date is not None:
            result["start_date"] = from_union([from_none, lambda x: x.isoformat()], self.start_date)
        if self.start_time is not None:
            result["start_time"] = from_union([from_none, from_str], self.start_time)
        return result


class TariffElement:
    price_components: List[PriceComponent]
    restrictions: Optional[Restrictions]

    def __init__(self, price_components: List[PriceComponent], restrictions: Optional[Restrictions]) -> None:
        self.price_components = price_components
        self.restrictions = restrictions

    @staticmethod
    def from_dict(obj: Any) -> 'TariffElement':
        assert isinstance(obj, dict)
        price_components = from_list(PriceComponent.from_dict, obj.get("price_components"))
        restrictions = from_union([from_none, Restrictions.from_dict], obj.get("restrictions"))
        return TariffElement(price_components, restrictions)

    def to_dict(self) -> dict:
        result: dict = {}
        result["price_components"] = from_list(lambda x: to_class(PriceComponent, x), self.price_components)
        if self.restrictions is not None:
            result["restrictions"] = from_union([from_none, lambda x: to_class(Restrictions, x)], self.restrictions)
        return result


class Tariff:
    currency: str
    elements: List[TariffElement]
    energy_mix: Optional[EnergyMix]
    id: str
    last_updated: str
    tariff_alt_text: Optional[List[DisplayText]]
    tariff_alt_url: Optional[str]

    def __init__(self, currency: str, elements: List[TariffElement], energy_mix: Optional[EnergyMix], id: str, last_updated: str, tariff_alt_text: Optional[List[DisplayText]], tariff_alt_url: Optional[str]) -> None:
        self.currency = currency
        self.elements = elements
        self.energy_mix = energy_mix
        self.id = id
        self.last_updated = last_updated
        self.tariff_alt_text = tariff_alt_text
        self.tariff_alt_url = tariff_alt_url

    @staticmethod
    def from_dict(obj: Any) -> 'Tariff':
        assert isinstance(obj, dict)
        currency = from_str(obj.get("currency"))
        elements = from_list(TariffElement.from_dict, obj.get("elements"))
        energy_mix = from_union([from_none, EnergyMix.from_dict], obj.get("energy_mix"))
        id = from_str(obj.get("id"))
        last_updated = from_str(obj.get("last_updated"))
        tariff_alt_text = from_union([from_none, lambda x: from_list(DisplayText.from_dict, x)], obj.get("tariff_alt_text"))
        tariff_alt_url = from_union([from_none, from_str], obj.get("tariff_alt_url"))
        return Tariff(currency, elements, energy_mix, id, last_updated, tariff_alt_text, tariff_alt_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["currency"] = from_str(self.currency)
        result["elements"] = from_list(lambda x: to_class(TariffElement, x), self.elements)
        if self.energy_mix is not None:
            result["energy_mix"] = from_union([from_none, lambda x: to_class(EnergyMix, x)], self.energy_mix)
        result["id"] = from_str(self.id)
        result["last_updated"] = from_str(self.last_updated)
        if self.tariff_alt_text is not None:
            result["tariff_alt_text"] = from_union([from_none, lambda x: from_list(lambda x: to_class(DisplayText, x), x)], self.tariff_alt_text)
        if self.tariff_alt_url is not None:
            result["tariff_alt_url"] = from_union([from_none, from_str], self.tariff_alt_url)
        return result


class Cdr:
    auth_id: str
    auth_method: AuthMethod
    charging_periods: List[ChargingPeriod]
    currency: str
    id: str
    last_updated: str
    location: CdrLocation
    meter_id: Optional[str]
    remark: Optional[str]
    start_date_time: str
    stop_date_time: str
    tariffs: Optional[List[Tariff]]
    total_cost: float
    total_energy: float
    total_parking_time: Optional[float]
    total_time: float

    def __init__(self, auth_id: str, auth_method: AuthMethod, charging_periods: List[ChargingPeriod], currency: str, id: str, last_updated: str, location: CdrLocation, meter_id: Optional[str], remark: Optional[str], start_date_time: str, stop_date_time: str, tariffs: Optional[List[Tariff]], total_cost: float, total_energy: float, total_parking_time: Optional[float], total_time: float) -> None:
        self.auth_id = auth_id
        self.auth_method = auth_method
        self.charging_periods = charging_periods
        self.currency = currency
        self.id = id
        self.last_updated = last_updated
        self.location = location
        self.meter_id = meter_id
        self.remark = remark
        self.start_date_time = start_date_time
        self.stop_date_time = stop_date_time
        self.tariffs = tariffs
        self.total_cost = total_cost
        self.total_energy = total_energy
        self.total_parking_time = total_parking_time
        self.total_time = total_time

    @staticmethod
    def from_dict(obj: Any) -> 'Cdr':
        assert isinstance(obj, dict)
        auth_id = from_str(obj.get("auth_id"))
        auth_method = AuthMethod(obj.get("auth_method"))
        charging_periods = from_list(ChargingPeriod.from_dict, obj.get("charging_periods"))
        currency = from_str(obj.get("currency"))
        id = from_str(obj.get("id"))
        last_updated = from_str(obj.get("last_updated"))
        location = CdrLocation.from_dict(obj.get("location"))
        meter_id = from_union([from_none, from_str], obj.get("meter_id"))
        remark = from_union([from_none, from_str], obj.get("remark"))
        start_date_time = from_str(obj.get("start_date_time"))
        stop_date_time = from_str(obj.get("stop_date_time"))
        tariffs = from_union([from_none, lambda x: from_list(Tariff.from_dict, x)], obj.get("tariffs"))
        total_cost = from_float(obj.get("total_cost"))
        total_energy = from_float(obj.get("total_energy"))
        total_parking_time = from_union([from_none, from_float], obj.get("total_parking_time"))
        total_time = from_float(obj.get("total_time"))
        return Cdr(auth_id, auth_method, charging_periods, currency, id, last_updated, location, meter_id, remark, start_date_time, stop_date_time, tariffs, total_cost, total_energy, total_parking_time, total_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["auth_id"] = from_str(self.auth_id)
        result["auth_method"] = to_enum(AuthMethod, self.auth_method)
        result["charging_periods"] = from_list(lambda x: to_class(ChargingPeriod, x), self.charging_periods)
        result["currency"] = from_str(self.currency)
        result["id"] = from_str(self.id)
        result["last_updated"] = from_str(self.last_updated)
        result["location"] = to_class(CdrLocation, self.location)
        if self.meter_id is not None:
            result["meter_id"] = from_union([from_none, from_str], self.meter_id)
        if self.remark is not None:
            result["remark"] = from_union([from_none, from_str], self.remark)
        result["start_date_time"] = from_str(self.start_date_time)
        result["stop_date_time"] = from_str(self.stop_date_time)
        if self.tariffs is not None:
            result["tariffs"] = from_union([from_none, lambda x: from_list(lambda x: to_class(Tariff, x), x)], self.tariffs)
        result["total_cost"] = to_float(self.total_cost)
        result["total_energy"] = to_float(self.total_energy)
        if self.total_parking_time is not None:
            result["total_parking_time"] = from_union([from_none, to_float], self.total_parking_time)
        result["total_time"] = to_float(self.total_time)
        return result


class Credentials:
    business_details: Optional[BusinessDetails]
    country_code: Optional[str]
    party_id: Optional[str]
    token: Optional[str]
    url: Optional[str]

    def __init__(self, business_details: Optional[BusinessDetails], country_code: Optional[str], party_id: Optional[str], token: Optional[str], url: Optional[str]) -> None:
        self.business_details = business_details
        self.country_code = country_code
        self.party_id = party_id
        self.token = token
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'Credentials':
        assert isinstance(obj, dict)
        business_details = from_union([from_none, BusinessDetails.from_dict], obj.get("business_details"))
        country_code = from_union([from_str, from_none], obj.get("country_code"))
        party_id = from_union([from_str, from_none], obj.get("party_id"))
        token = from_union([from_str, from_none], obj.get("token"))
        url = from_union([from_str, from_none], obj.get("url"))
        return Credentials(business_details, country_code, party_id, token, url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.business_details is not None:
            result["business_details"] = from_union([from_none, lambda x: to_class(BusinessDetails, x)], self.business_details)
        if self.country_code is not None:
            result["country_code"] = from_union([from_str, from_none], self.country_code)
        if self.party_id is not None:
            result["party_id"] = from_union([from_str, from_none], self.party_id)
        if self.token is not None:
            result["token"] = from_union([from_str, from_none], self.token)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        return result


class Location:
    address: Optional[str]
    charging_when_closed: Optional[bool]
    city: Optional[str]
    coordinates: Optional[GeoLocation]
    country: Optional[str]
    directions: Optional[List[DisplayText]]
    energy_mix: Optional[EnergyMix]
    evses: Optional[List[Evse]]
    facilities: Optional[List[Facility]]
    id: Optional[str]
    images: Optional[List[Image]]
    last_updated: Optional[str]
    name: Optional[str]
    opening_times: Optional[Hours]
    operator: Optional[BusinessDetails]
    owner: Optional[BusinessDetails]
    postal_code: Optional[str]
    related_locations: Optional[List[RelatedLocation]]
    suboperator: Optional[BusinessDetails]
    time_zone: Optional[str]
    type: Optional[LocationType]

    def __init__(self, address: Optional[str], charging_when_closed: Optional[bool], city: Optional[str], coordinates: Optional[GeoLocation], country: Optional[str], directions: Optional[List[DisplayText]], energy_mix: Optional[EnergyMix], evses: Optional[List[Evse]], facilities: Optional[List[Facility]], id: Optional[str], images: Optional[List[Image]], last_updated: Optional[str], name: Optional[str], opening_times: Optional[Hours], operator: Optional[BusinessDetails], owner: Optional[BusinessDetails], postal_code: Optional[str], related_locations: Optional[List[RelatedLocation]], suboperator: Optional[BusinessDetails], time_zone: Optional[str], type: Optional[LocationType]) -> None:
        self.address = address
        self.charging_when_closed = charging_when_closed
        self.city = city
        self.coordinates = coordinates
        self.country = country
        self.directions = directions
        self.energy_mix = energy_mix
        self.evses = evses
        self.facilities = facilities
        self.id = id
        self.images = images
        self.last_updated = last_updated
        self.name = name
        self.opening_times = opening_times
        self.operator = operator
        self.owner = owner
        self.postal_code = postal_code
        self.related_locations = related_locations
        self.suboperator = suboperator
        self.time_zone = time_zone
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Location':
        assert isinstance(obj, dict)
        address = from_union([from_str, from_none], obj.get("address"))
        charging_when_closed = from_union([from_none, from_bool], obj.get("charging_when_closed"))
        city = from_union([from_str, from_none], obj.get("city"))
        coordinates = from_union([from_none, GeoLocation.from_dict], obj.get("coordinates"))
        country = from_union([from_str, from_none], obj.get("country"))
        directions = from_union([from_none, lambda x: from_list(DisplayText.from_dict, x)], obj.get("directions"))
        energy_mix = from_union([from_none, EnergyMix.from_dict], obj.get("energy_mix"))
        evses = from_union([from_none, lambda x: from_list(Evse.from_dict, x)], obj.get("evses"))
        facilities = from_union([from_none, lambda x: from_list(Facility, x)], obj.get("facilities"))
        id = from_union([from_str, from_none], obj.get("id"))
        images = from_union([from_none, lambda x: from_list(Image.from_dict, x)], obj.get("images"))
        last_updated = from_union([from_str, from_none], obj.get("last_updated"))
        name = from_union([from_none, from_str], obj.get("name"))
        opening_times = from_union([from_none, Hours.from_dict], obj.get("opening_times"))
        operator = from_union([from_none, BusinessDetails.from_dict], obj.get("operator"))
        owner = from_union([from_none, BusinessDetails.from_dict], obj.get("owner"))
        postal_code = from_union([from_str, from_none], obj.get("postal_code"))
        related_locations = from_union([from_none, lambda x: from_list(RelatedLocation.from_dict, x)], obj.get("related_locations"))
        suboperator = from_union([from_none, BusinessDetails.from_dict], obj.get("suboperator"))
        time_zone = from_union([from_none, from_str], obj.get("time_zone"))
        type = from_union([LocationType, from_none], obj.get("type"))
        return Location(address, charging_when_closed, city, coordinates, country, directions, energy_mix, evses, facilities, id, images, last_updated, name, opening_times, operator, owner, postal_code, related_locations, suboperator, time_zone, type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.address is not None:
            result["address"] = from_union([from_str, from_none], self.address)
        if self.charging_when_closed is not None:
            result["charging_when_closed"] = from_union([from_none, from_bool], self.charging_when_closed)
        if self.city is not None:
            result["city"] = from_union([from_str, from_none], self.city)
        if self.coordinates is not None:
            result["coordinates"] = from_union([from_none, lambda x: to_class(GeoLocation, x)], self.coordinates)
        if self.country is not None:
            result["country"] = from_union([from_str, from_none], self.country)
        if self.directions is not None:
            result["directions"] = from_union([from_none, lambda x: from_list(lambda x: to_class(DisplayText, x), x)], self.directions)
        if self.energy_mix is not None:
            result["energy_mix"] = from_union([from_none, lambda x: to_class(EnergyMix, x)], self.energy_mix)
        if self.evses is not None:
            result["evses"] = from_union([from_none, lambda x: from_list(lambda x: to_class(Evse, x), x)], self.evses)
        if self.facilities is not None:
            result["facilities"] = from_union([from_none, lambda x: from_list(lambda x: to_enum(Facility, x), x)], self.facilities)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.images is not None:
            result["images"] = from_union([from_none, lambda x: from_list(lambda x: to_class(Image, x), x)], self.images)
        if self.last_updated is not None:
            result["last_updated"] = from_union([from_str, from_none], self.last_updated)
        if self.name is not None:
            result["name"] = from_union([from_none, from_str], self.name)
        if self.opening_times is not None:
            result["opening_times"] = from_union([from_none, lambda x: to_class(Hours, x)], self.opening_times)
        if self.operator is not None:
            result["operator"] = from_union([from_none, lambda x: to_class(BusinessDetails, x)], self.operator)
        if self.owner is not None:
            result["owner"] = from_union([from_none, lambda x: to_class(BusinessDetails, x)], self.owner)
        if self.postal_code is not None:
            result["postal_code"] = from_union([from_str, from_none], self.postal_code)
        if self.related_locations is not None:
            result["related_locations"] = from_union([from_none, lambda x: from_list(lambda x: to_class(RelatedLocation, x), x)], self.related_locations)
        if self.suboperator is not None:
            result["suboperator"] = from_union([from_none, lambda x: to_class(BusinessDetails, x)], self.suboperator)
        if self.time_zone is not None:
            result["time_zone"] = from_union([from_none, from_str], self.time_zone)
        if self.type is not None:
            result["type"] = from_union([lambda x: to_enum(LocationType, x), from_none], self.type)
        return result


class SessionLocation:
    id: str
    type: LocationType
    address: str
    city: str
    postal_code: str
    country: str
    coordinates: GeoLocation
    last_updated: str
    charging_when_closed: Optional[bool]
    directions: Optional[List[DisplayText]]
    energy_mix: Optional[EnergyMix]
    evses: Optional[List[Evse]]
    facilities: Optional[List[Facility]]
    images: Optional[List[Image]]
    name: Optional[str]
    opening_times: Optional[Hours]
    operator: Optional[BusinessDetails]
    owner: Optional[BusinessDetails]
    related_locations: Optional[List[RelatedLocation]]
    suboperator: Optional[BusinessDetails]
    time_zone: Optional[str]

    def __init__(self, id: str, type: LocationType, address: str, city: str, postal_code: str, country: str, coordinates: GeoLocation, last_updated: str, charging_when_closed: Optional[bool], directions: Optional[List[DisplayText]], energy_mix: Optional[EnergyMix], evses: Optional[List[Evse]], facilities: Optional[List[Facility]], images: Optional[List[Image]], name: Optional[str], opening_times: Optional[Hours], operator: Optional[BusinessDetails], owner: Optional[BusinessDetails], related_locations: Optional[List[RelatedLocation]], suboperator: Optional[BusinessDetails], time_zone: Optional[str]) -> None:
        self.id = id
        self.type = type
        self.address = address
        self.city = city
        self.postal_code = postal_code
        self.country = country
        self.coordinates = coordinates
        self.last_updated = last_updated
        self.charging_when_closed = charging_when_closed
        self.directions = directions
        self.energy_mix = energy_mix
        self.evses = evses
        self.facilities = facilities
        self.images = images
        self.name = name
        self.opening_times = opening_times
        self.operator = operator
        self.owner = owner
        self.related_locations = related_locations
        self.suboperator = suboperator
        self.time_zone = time_zone

    @staticmethod
    def from_dict(obj: Any) -> 'SessionLocation':
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        type = LocationType(obj.get("type"))
        address = from_str(obj.get("address"))
        city = from_str(obj.get("city"))
        postal_code = from_str(obj.get("postal_code"))
        country = from_str(obj.get("country"))
        coordinates = GeoLocation.from_dict(obj.get("coordinates"))
        last_updated = from_str(obj.get("last_updated"))
        charging_when_closed = from_union([from_none, from_bool], obj.get("charging_when_closed"))
        directions = from_union([from_none, lambda x: from_list(DisplayText.from_dict, x)], obj.get("directions"))
        energy_mix = from_union([from_none, EnergyMix.from_dict], obj.get("energy_mix"))
        evses = from_union([from_none, lambda x: from_list(Evse.from_dict, x)], obj.get("evses"))
        facilities = from_union([from_none, lambda x: from_list(Facility, x)], obj.get("facilities"))
        images = from_union([from_none, lambda x: from_list(Image.from_dict, x)], obj.get("images"))
        name = from_union([from_none, from_str], obj.get("name"))
        opening_times = from_union([from_none, Hours.from_dict], obj.get("opening_times"))
        operator = from_union([from_none, BusinessDetails.from_dict], obj.get("operator"))
        owner = from_union([from_none, BusinessDetails.from_dict], obj.get("owner"))
        related_locations = from_union([from_none, lambda x: from_list(RelatedLocation.from_dict, x)], obj.get("related_locations"))
        suboperator = from_union([from_none, BusinessDetails.from_dict], obj.get("suboperator"))
        time_zone = from_union([from_none, from_str], obj.get("time_zone"))
        return SessionLocation(id, type, address, city, postal_code, country, coordinates, last_updated, charging_when_closed, directions, energy_mix, evses, facilities, images, name, opening_times, operator, owner, related_locations, suboperator, time_zone)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(self.id)
        result["type"] = to_enum(LocationType, self.type)
        result["address"] = from_str(self.address)
        result["city"] = from_str(self.city)
        result["postal_code"] = from_str(self.postal_code)
        result["country"] = from_str(self.country)
        result["coordinates"] = to_class(GeoLocation, self.coordinates)
        result["last_updated"] = from_str(self.last_updated)
        if self.charging_when_closed is not None:
            result["charging_when_closed"] = from_union([from_none, from_bool], self.charging_when_closed)
        if self.directions is not None:
            result["directions"] = from_union([from_none, lambda x: from_list(lambda x: to_class(DisplayText, x), x)], self.directions)
        if self.energy_mix is not None:
            result["energy_mix"] = from_union([from_none, lambda x: to_class(EnergyMix, x)], self.energy_mix)
        if self.evses is not None:
            result["evses"] = from_union([from_none, lambda x: from_list(lambda x: to_class(Evse, x), x)], self.evses)
        if self.facilities is not None:
            result["facilities"] = from_union([from_none, lambda x: from_list(lambda x: to_enum(Facility, x), x)], self.facilities)
        if self.images is not None:
            result["images"] = from_union([from_none, lambda x: from_list(lambda x: to_class(Image, x), x)], self.images)
        if self.name is not None:
            result["name"] = from_union([from_none, from_str], self.name)
        if self.opening_times is not None:
            result["opening_times"] = from_union([from_none, lambda x: to_class(Hours, x)], self.opening_times)
        if self.operator is not None:
            result["operator"] = from_union([from_none, lambda x: to_class(BusinessDetails, x)], self.operator)
        if self.owner is not None:
            result["owner"] = from_union([from_none, lambda x: to_class(BusinessDetails, x)], self.owner)
        if self.related_locations is not None:
            result["related_locations"] = from_union([from_none, lambda x: from_list(lambda x: to_class(RelatedLocation, x), x)], self.related_locations)
        if self.suboperator is not None:
            result["suboperator"] = from_union([from_none, lambda x: to_class(BusinessDetails, x)], self.suboperator)
        if self.time_zone is not None:
            result["time_zone"] = from_union([from_none, from_str], self.time_zone)
        return result


class Status(Enum):
    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"
    INVALID = "INVALID"
    PENDING = "PENDING"


class Session:
    auth_id: Optional[str]
    auth_method: Optional[AuthMethod]
    charging_periods: Optional[List[ChargingPeriod]]
    currency: Optional[str]
    end_datetime: Optional[str]
    id: Optional[str]
    kwh: Optional[float]
    last_updated: Optional[str]
    location: Optional[SessionLocation]
    meter_id: Optional[str]
    start_datetime: Optional[str]
    status: Optional[Status]
    total_cost: Optional[float]

    def __init__(self, auth_id: Optional[str], auth_method: Optional[AuthMethod], charging_periods: Optional[List[ChargingPeriod]], currency: Optional[str], end_datetime: Optional[str], id: Optional[str], kwh: Optional[float], last_updated: Optional[str], location: Optional[SessionLocation], meter_id: Optional[str], start_datetime: Optional[str], status: Optional[Status], total_cost: Optional[float]) -> None:
        self.auth_id = auth_id
        self.auth_method = auth_method
        self.charging_periods = charging_periods
        self.currency = currency
        self.end_datetime = end_datetime
        self.id = id
        self.kwh = kwh
        self.last_updated = last_updated
        self.location = location
        self.meter_id = meter_id
        self.start_datetime = start_datetime
        self.status = status
        self.total_cost = total_cost

    @staticmethod
    def from_dict(obj: Any) -> 'Session':
        assert isinstance(obj, dict)
        auth_id = from_union([from_str, from_none], obj.get("auth_id"))
        auth_method = from_union([AuthMethod, from_none], obj.get("auth_method"))
        charging_periods = from_union([from_none, lambda x: from_list(ChargingPeriod.from_dict, x)], obj.get("charging_periods"))
        currency = from_union([from_str, from_none], obj.get("currency"))
        end_datetime = from_union([from_none, from_str], obj.get("end_datetime"))
        id = from_union([from_str, from_none], obj.get("id"))
        kwh = from_union([from_none, from_float], obj.get("kwh"))
        last_updated = from_union([from_str, from_none], obj.get("last_updated"))
        location = from_union([SessionLocation.from_dict, from_none], obj.get("location"))
        meter_id = from_union([from_none, from_str], obj.get("meter_id"))
        start_datetime = from_union([from_str, from_none], obj.get("start_datetime"))
        status = from_union([Status, from_none], obj.get("status"))
        total_cost = from_union([from_none, from_float], obj.get("total_cost"))
        return Session(auth_id, auth_method, charging_periods, currency, end_datetime, id, kwh, last_updated, location, meter_id, start_datetime, status, total_cost)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.auth_id is not None:
            result["auth_id"] = from_union([from_str, from_none], self.auth_id)
        if self.auth_method is not None:
            result["auth_method"] = from_union([lambda x: to_enum(AuthMethod, x), from_none], self.auth_method)
        if self.charging_periods is not None:
            result["charging_periods"] = from_union([from_none, lambda x: from_list(lambda x: to_class(ChargingPeriod, x), x)], self.charging_periods)
        if self.currency is not None:
            result["currency"] = from_union([from_str, from_none], self.currency)
        if self.end_datetime is not None:
            result["end_datetime"] = from_union([from_none, from_str], self.end_datetime)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.kwh is not None:
            result["kwh"] = from_union([from_none, to_float], self.kwh)
        if self.last_updated is not None:
            result["last_updated"] = from_union([from_str, from_none], self.last_updated)
        if self.location is not None:
            result["location"] = from_union([lambda x: to_class(SessionLocation, x), from_none], self.location)
        if self.meter_id is not None:
            result["meter_id"] = from_union([from_none, from_str], self.meter_id)
        if self.start_datetime is not None:
            result["start_datetime"] = from_union([from_str, from_none], self.start_datetime)
        if self.status is not None:
            result["status"] = from_union([lambda x: to_enum(Status, x), from_none], self.status)
        if self.total_cost is not None:
            result["total_cost"] = from_union([from_none, to_float], self.total_cost)
        return result


class TokenType(Enum):
    OTHER = "OTHER"
    RFID = "RFID"


class Whitelist(Enum):
    ALLOWED = "ALLOWED"
    ALLOWED_OFFLINE = "ALLOWED_OFFLINE"
    ALWAYS = "ALWAYS"
    NEVER = "NEVER"


class Token:
    auth_id: Optional[str]
    issuer: Optional[str]
    language: Optional[str]
    last_updated: Optional[str]
    type: Optional[TokenType]
    uid: Optional[str]
    valid: Optional[bool]
    visual_number: Optional[str]
    whitelist: Optional[Whitelist]

    def __init__(self, auth_id: Optional[str], issuer: Optional[str], language: Optional[str], last_updated: Optional[str], type: Optional[TokenType], uid: Optional[str], valid: Optional[bool], visual_number: Optional[str], whitelist: Optional[Whitelist]) -> None:
        self.auth_id = auth_id
        self.issuer = issuer
        self.language = language
        self.last_updated = last_updated
        self.type = type
        self.uid = uid
        self.valid = valid
        self.visual_number = visual_number
        self.whitelist = whitelist

    @staticmethod
    def from_dict(obj: Any) -> 'Token':
        assert isinstance(obj, dict)
        auth_id = from_union([from_str, from_none], obj.get("auth_id"))
        issuer = from_union([from_str, from_none], obj.get("issuer"))
        language = from_union([from_str, from_none], obj.get("language"))
        last_updated = from_union([from_str, from_none], obj.get("last_updated"))
        type = from_union([TokenType, from_none], obj.get("type"))
        uid = from_union([from_str, from_none], obj.get("uid"))
        valid = from_union([from_none, from_bool], obj.get("valid"))
        visual_number = from_union([from_str, from_none], obj.get("visual_number"))
        whitelist = from_union([Whitelist, from_none], obj.get("whitelist"))
        return Token(auth_id, issuer, language, last_updated, type, uid, valid, visual_number, whitelist)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.auth_id is not None:
            result["auth_id"] = from_union([from_str, from_none], self.auth_id)
        if self.issuer is not None:
            result["issuer"] = from_union([from_str, from_none], self.issuer)
        if self.language is not None:
            result["language"] = from_union([from_str, from_none], self.language)
        if self.last_updated is not None:
            result["last_updated"] = from_union([from_str, from_none], self.last_updated)
        if self.type is not None:
            result["type"] = from_union([lambda x: to_enum(TokenType, x), from_none], self.type)
        if self.uid is not None:
            result["uid"] = from_union([from_str, from_none], self.uid)
        if self.valid is not None:
            result["valid"] = from_union([from_none, from_bool], self.valid)
        if self.visual_number is not None:
            result["visual_number"] = from_union([from_str, from_none], self.visual_number)
        if self.whitelist is not None:
            result["whitelist"] = from_union([lambda x: to_enum(Whitelist, x), from_none], self.whitelist)
        return result


class V211:
    cdr: Optional[Cdr]
    connector: Optional[Connector]
    credentials: Optional[Credentials]
    evse: Optional[Evse]
    location: Optional[Location]
    session: Optional[Session]
    tariff: Optional[Tariff]
    token: Optional[Token]

    def __init__(self, cdr: Optional[Cdr], connector: Optional[Connector], credentials: Optional[Credentials], evse: Optional[Evse], location: Optional[Location], session: Optional[Session], tariff: Optional[Tariff], token: Optional[Token]) -> None:
        self.cdr = cdr
        self.connector = connector
        self.credentials = credentials
        self.evse = evse
        self.location = location
        self.session = session
        self.tariff = tariff
        self.token = token

    @staticmethod
    def from_dict(obj: Any) -> 'V211':
        assert isinstance(obj, dict)
        cdr = from_union([Cdr.from_dict, from_none], obj.get("cdr"))
        connector = from_union([Connector.from_dict, from_none], obj.get("connector"))
        credentials = from_union([Credentials.from_dict, from_none], obj.get("credentials"))
        evse = from_union([Evse.from_dict, from_none], obj.get("evse"))
        location = from_union([Location.from_dict, from_none], obj.get("location"))
        session = from_union([Session.from_dict, from_none], obj.get("session"))
        tariff = from_union([Tariff.from_dict, from_none], obj.get("tariff"))
        token = from_union([Token.from_dict, from_none], obj.get("token"))
        return V211(cdr, connector, credentials, evse, location, session, tariff, token)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.cdr is not None:
            result["cdr"] = from_union([lambda x: to_class(Cdr, x), from_none], self.cdr)
        if self.connector is not None:
            result["connector"] = from_union([lambda x: to_class(Connector, x), from_none], self.connector)
        if self.credentials is not None:
            result["credentials"] = from_union([lambda x: to_class(Credentials, x), from_none], self.credentials)
        if self.evse is not None:
            result["evse"] = from_union([lambda x: to_class(Evse, x), from_none], self.evse)
        if self.location is not None:
            result["location"] = from_union([lambda x: to_class(Location, x), from_none], self.location)
        if self.session is not None:
            result["session"] = from_union([lambda x: to_class(Session, x), from_none], self.session)
        if self.tariff is not None:
            result["tariff"] = from_union([lambda x: to_class(Tariff, x), from_none], self.tariff)
        if self.token is not None:
            result["token"] = from_union([lambda x: to_class(Token, x), from_none], self.token)
        return result


def v211_from_dict(s: Any) -> V211:
    return V211.from_dict(s)


def v211_to_dict(x: V211) -> Any:
    return to_class(V211, x)
