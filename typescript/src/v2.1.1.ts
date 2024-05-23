// To parse this data:
//
//   import { Convert, V211 } from "./file";
//
//   const v211 = Convert.toV211(json);
//
// These functions will throw an error if the JSON doesn't
// match the expected interface, even if the JSON is valid.

export interface V211 {
    cdr?:         Cdr;
    connector?:   Connector;
    credentials?: Credentials;
    evse?:        Evse;
    location?:    Location;
    session?:     Session;
    tariff?:      Tariff;
    token?:       Token;
    [property: string]: any;
}

export interface Cdr {
    auth_id:             string;
    auth_method:         AuthMethod;
    charging_periods:    ChargingPeriod[];
    currency:            string;
    id:                  string;
    last_updated:        string;
    location:            CdrLocation;
    meter_id?:           null | string;
    remark?:             null | string;
    start_date_time:     string;
    stop_date_time:      string;
    tariffs?:            Tariff[] | null;
    total_cost:          number;
    total_energy:        number;
    total_parking_time?: number | null;
    total_time:          number;
}

export enum AuthMethod {
    AuthRequest = "AUTH_REQUEST",
    Whitelist = "WHITELIST",
}

export interface ChargingPeriod {
    dimensions:      Dimension[];
    start_date_time: string;
}

export interface Dimension {
    type:   DimensionType;
    volume: number;
}

export enum DimensionType {
    Energy = "ENERGY",
    Flat = "FLAT",
    MaxCurrent = "MAX_CURRENT",
    MinCurrent = "MIN_CURRENT",
    ParkingTime = "PARKING_TIME",
    Time = "TIME",
}

export interface CdrLocation {
    id:                    string;
    type:                  LocationType;
    address:               string;
    city:                  string;
    postal_code:           string;
    country:               string;
    coordinates:           GeoLocation;
    last_updated:          string;
    charging_when_closed?: boolean | null;
    directions?:           DisplayText[] | null;
    energy_mix?:           EnergyMix | null;
    evses?:                Evse[] | null;
    facilities?:           Facility[] | null;
    images?:               Image[] | null;
    name?:                 null | string;
    opening_times?:        Hours | null;
    operator?:             BusinessDetails | null;
    owner?:                BusinessDetails | null;
    related_locations?:    RelatedLocation[] | null;
    suboperator?:          BusinessDetails | null;
    time_zone?:            null | string;
}

export interface GeoLocation {
    latitude?:  string;
    longitude?: string;
}

export interface DisplayText {
    language: string;
    text:     string;
}

export interface EnergyMix {
    energy_product_name?: null | string;
    energy_sources?:      EnergySource[] | null;
    environ_impact?:      EnvironImpact[] | null;
    is_green_energy:      boolean;
    supplier_name?:       null | string;
}

export interface EnergySource {
    percentage: number;
    source:     EnergySourceSource;
}

export enum EnergySourceSource {
    Coal = "COAL",
    Gas = "GAS",
    GeneralFossil = "GENERAL_FOSSIL",
    GeneralGreen = "GENERAL_GREEN",
    Nuclear = "NUCLEAR",
    Solar = "SOLAR",
    Water = "WATER",
    Wind = "WIND",
}

export interface EnvironImpact {
    amount: number;
    source: EnvironImpactSource;
}

export enum EnvironImpactSource {
    CarbonDioxide = "CARBON_DIOXIDE",
    NuclearWaste = "NUCLEAR_WASTE",
}

export interface Evse {
    capabilities?:         Capability[] | null;
    connectors?:           Connector[];
    coordinates?:          GeoLocation | null;
    directions?:           DisplayText[] | null;
    evse_id?:              null | string;
    floor_level?:          null | string;
    images?:               Image[] | null;
    last_updated?:         string;
    parking_restrictions?: ParkingRestriction[] | null;
    physical_reference?:   null | string;
    status?:               EvseStatus;
    status_schedule?:      StatusSchedule[] | null;
    uid?:                  string;
}

export enum Capability {
    ChargingProfileCapable = "CHARGING_PROFILE_CAPABLE",
    CreditCardPayable = "CREDIT_CARD_PAYABLE",
    RFIDReader = "RFID_READER",
    RemoteStartStopCapable = "REMOTE_START_STOP_CAPABLE",
    Reservable = "RESERVABLE",
    UnlockCapable = "UNLOCK_CAPABLE",
}

export interface Connector {
    amperage?:             number;
    format?:               Format;
    id?:                   string;
    last_updated?:         string;
    power_type?:           PowerType;
    standard?:             Standard;
    tariff_id?:            null | string;
    terms_and_conditions?: null | string;
    voltage?:              number;
}

export enum Format {
    Cable = "CABLE",
    Socket = "SOCKET",
}

export enum PowerType {
    AC1_Phase = "AC_1_PHASE",
    AC3_Phase = "AC_3_PHASE",
    Dc = "DC",
}

export enum Standard {
    Chademo = "CHADEMO",
    DomesticA = "DOMESTIC_A",
    DomesticB = "DOMESTIC_B",
    DomesticC = "DOMESTIC_C",
    DomesticD = "DOMESTIC_D",
    DomesticE = "DOMESTIC_E",
    DomesticF = "DOMESTIC_F",
    DomesticG = "DOMESTIC_G",
    DomesticH = "DOMESTIC_H",
    DomesticI = "DOMESTIC_I",
    DomesticJ = "DOMESTIC_J",
    DomesticK = "DOMESTIC_K",
    DomesticL = "DOMESTIC_L",
    IEC60309_2_Single16 = "IEC_60309_2_single_16",
    IEC60309_2_Three16 = "IEC_60309_2_three_16",
    IEC60309_2_Three32 = "IEC_60309_2_three_32",
    IEC60309_2_Three64 = "IEC_60309_2_three_64",
    IEC62196_T1 = "IEC_62196_T1",
    IEC62196_T1Combo = "IEC_62196_T1_COMBO",
    IEC62196_T2 = "IEC_62196_T2",
    IEC62196_T2Combo = "IEC_62196_T2_COMBO",
    IEC62196_T3A = "IEC_62196_T3A",
    IEC62196_T3C = "IEC_62196_T3C",
    TeslaR = "TESLA_R",
    TeslaS = "TESLA_S",
}

export interface Image {
    category:   Category;
    height?:    number | null;
    thumbnail?: null | string;
    type:       string;
    url:        string;
    width?:     number | null;
}

export enum Category {
    Charger = "CHARGER",
    Entrance = "ENTRANCE",
    Location = "LOCATION",
    Network = "NETWORK",
    Operator = "OPERATOR",
    Other = "OTHER",
    Owner = "OWNER",
}

export enum ParkingRestriction {
    Customers = "CUSTOMERS",
    Disabled = "DISABLED",
    EvOnly = "EV_ONLY",
    Motorcycles = "MOTORCYCLES",
    Plugged = "PLUGGED",
}

export enum EvseStatus {
    Available = "AVAILABLE",
    Blocked = "BLOCKED",
    Charging = "CHARGING",
    Inoperative = "INOPERATIVE",
    Outoforder = "OUTOFORDER",
    Planned = "PLANNED",
    Removed = "REMOVED",
    Reserved = "RESERVED",
    Unknown = "UNKNOWN",
}

export interface StatusSchedule {
    period_begin: string;
    period_end?:  string;
    status:       EvseStatus;
}

export enum Facility {
    Airport = "AIRPORT",
    BusStop = "BUS_STOP",
    Cafe = "CAFE",
    CarpoolParking = "CARPOOL_PARKING",
    FuelStation = "FUEL_STATION",
    Hotel = "HOTEL",
    Mall = "MALL",
    Museum = "MUSEUM",
    Nature = "NATURE",
    RecreationArea = "RECREATION_AREA",
    Restaurant = "RESTAURANT",
    Sport = "SPORT",
    Supermarket = "SUPERMARKET",
    TaxiStand = "TAXI_STAND",
    TrainStation = "TRAIN_STATION",
    Wifi = "WIFI",
}

export interface Hours {
    exceptional_closings?: ExceptionalPeriod[] | null;
    exceptional_openings?: ExceptionalPeriod[] | null;
    regular_hours?:        RegularHours[] | null;
    twentyfourseven?:      boolean;
}

export interface ExceptionalPeriod {
    period_begin: string;
    period_end:   string;
}

export interface RegularHours {
    period_begin?: string;
    period_end?:   string;
    weekday?:      number;
}

export interface BusinessDetails {
    logo?:    Image | null;
    name:     string;
    website?: null | string;
}

export interface RelatedLocation {
    latitude?:  string;
    longitude?: string;
    name?:      DisplayText;
    [property: string]: any;
}

export enum LocationType {
    OnStreet = "ON_STREET",
    Other = "OTHER",
    ParkingGarage = "PARKING_GARAGE",
    ParkingLot = "PARKING_LOT",
    UndergroundGarage = "UNDERGROUND_GARAGE",
    Unknown = "UNKNOWN",
}

export interface Tariff {
    currency:         string;
    elements:         TariffElement[];
    energy_mix?:      EnergyMix | null;
    id:               string;
    last_updated:     string;
    tariff_alt_text?: DisplayText[] | null;
    tariff_alt_url?:  null | string;
}

export interface TariffElement {
    price_components: PriceComponent[];
    restrictions?:    Restrictions | null;
}

export interface PriceComponent {
    price:     number;
    step_size: number;
    type:      PriceComponentType;
}

export enum PriceComponentType {
    Energy = "ENERGY",
    Flat = "FLAT",
    ParkingTime = "PARKING_TIME",
    Time = "TIME",
}

export interface Restrictions {
    day_of_week?:  DayOfWeek[] | null;
    end_date?:     Date | null;
    end_time?:     null | string;
    max_duration?: number | null;
    max_kwh?:      number | null;
    max_power?:    number | null;
    min_duration?: number | null;
    min_kwh?:      number | null;
    min_power?:    number | null;
    start_date?:   Date | null;
    start_time?:   null | string;
}

export enum DayOfWeek {
    Friday = "FRIDAY",
    Monday = "MONDAY",
    Saturday = "SATURDAY",
    Sunday = "SUNDAY",
    Thursday = "THURSDAY",
    Tuesday = "TUESDAY",
    Wednesday = "WEDNESDAY",
}

export interface Credentials {
    business_details?: BusinessDetails;
    country_code?:     string;
    party_id?:         string;
    token?:            string;
    url?:              string;
}

export interface Location {
    address?:              string;
    charging_when_closed?: boolean | null;
    city?:                 string;
    coordinates?:          GeoLocation;
    country?:              string;
    directions?:           DisplayText[] | null;
    energy_mix?:           EnergyMix | null;
    evses?:                Evse[] | null;
    facilities?:           Facility[] | null;
    id?:                   string;
    images?:               Image[] | null;
    last_updated?:         string;
    name?:                 null | string;
    opening_times?:        Hours | null;
    operator?:             BusinessDetails | null;
    owner?:                BusinessDetails | null;
    postal_code?:          string;
    related_locations?:    RelatedLocation[] | null;
    suboperator?:          BusinessDetails | null;
    time_zone?:            null | string;
    type?:                 LocationType;
}

export interface Session {
    auth_id?:          string;
    auth_method?:      AuthMethod;
    charging_periods?: ChargingPeriod[] | null;
    currency?:         string;
    end_datetime?:     null | string;
    id?:               string;
    kwh?:              number;
    last_updated?:     string;
    location?:         SessionLocation;
    meter_id?:         null | string;
    start_datetime?:   string;
    status?:           Status;
    total_cost?:       number | null;
}

export interface SessionLocation {
    id:                    string;
    type:                  LocationType;
    address:               string;
    city:                  string;
    postal_code:           string;
    country:               string;
    coordinates:           GeoLocation;
    last_updated:          string;
    charging_when_closed?: boolean | null;
    directions?:           DisplayText[] | null;
    energy_mix?:           EnergyMix | null;
    evses?:                Evse[] | null;
    facilities?:           Facility[] | null;
    images?:               Image[] | null;
    name?:                 null | string;
    opening_times?:        Hours | null;
    operator?:             BusinessDetails | null;
    owner?:                BusinessDetails | null;
    related_locations?:    RelatedLocation[] | null;
    suboperator?:          BusinessDetails | null;
    time_zone?:            null | string;
}

export enum Status {
    Active = "ACTIVE",
    Completed = "COMPLETED",
    Invalid = "INVALID",
    Pending = "PENDING",
}

export interface Token {
    auth_id?:       string;
    issuer?:        string;
    language?:      string;
    last_updated?:  string;
    type?:          TokenType;
    uid?:           string;
    valid?:         boolean;
    visual_number?: string;
    whitelist?:     Whitelist;
}

export enum TokenType {
    Other = "OTHER",
    RFID = "RFID",
}

export enum Whitelist {
    Allowed = "ALLOWED",
    AllowedOffline = "ALLOWED_OFFLINE",
    Always = "ALWAYS",
    Never = "NEVER",
}

// Converts JSON strings to/from your types
// and asserts the results of JSON.parse at runtime
export class Convert {
    public static toV211(json: string): V211 {
        return cast(JSON.parse(json), r("V211"));
    }

    public static v211ToJson(value: V211): string {
        return JSON.stringify(uncast(value, r("V211")), null, 2);
    }
}

function invalidValue(typ: any, val: any, key: any, parent: any = ''): never {
    const prettyTyp = prettyTypeName(typ);
    const parentText = parent ? ` on ${parent}` : '';
    const keyText = key ? ` for key "${key}"` : '';
    throw Error(`Invalid value${keyText}${parentText}. Expected ${prettyTyp} but got ${JSON.stringify(val)}`);
}

function prettyTypeName(typ: any): string {
    if (Array.isArray(typ)) {
        if (typ.length === 2 && typ[0] === undefined) {
            return `an optional ${prettyTypeName(typ[1])}`;
        } else {
            return `one of [${typ.map(a => { return prettyTypeName(a); }).join(", ")}]`;
        }
    } else if (typeof typ === "object" && typ.literal !== undefined) {
        return typ.literal;
    } else {
        return typeof typ;
    }
}

function jsonToJSProps(typ: any): any {
    if (typ.jsonToJS === undefined) {
        const map: any = {};
        typ.props.forEach((p: any) => map[p.json] = { key: p.js, typ: p.typ });
        typ.jsonToJS = map;
    }
    return typ.jsonToJS;
}

function jsToJSONProps(typ: any): any {
    if (typ.jsToJSON === undefined) {
        const map: any = {};
        typ.props.forEach((p: any) => map[p.js] = { key: p.json, typ: p.typ });
        typ.jsToJSON = map;
    }
    return typ.jsToJSON;
}

function transform(val: any, typ: any, getProps: any, key: any = '', parent: any = ''): any {
    function transformPrimitive(typ: string, val: any): any {
        if (typeof typ === typeof val) return val;
        return invalidValue(typ, val, key, parent);
    }

    function transformUnion(typs: any[], val: any): any {
        // val must validate against one typ in typs
        const l = typs.length;
        for (let i = 0; i < l; i++) {
            const typ = typs[i];
            try {
                return transform(val, typ, getProps);
            } catch (_) {}
        }
        return invalidValue(typs, val, key, parent);
    }

    function transformEnum(cases: string[], val: any): any {
        if (cases.indexOf(val) !== -1) return val;
        return invalidValue(cases.map(a => { return l(a); }), val, key, parent);
    }

    function transformArray(typ: any, val: any): any {
        // val must be an array with no invalid elements
        if (!Array.isArray(val)) return invalidValue(l("array"), val, key, parent);
        return val.map(el => transform(el, typ, getProps));
    }

    function transformDate(val: any): any {
        if (val === null) {
            return null;
        }
        const d = new Date(val);
        if (isNaN(d.valueOf())) {
            return invalidValue(l("Date"), val, key, parent);
        }
        return d;
    }

    function transformObject(props: { [k: string]: any }, additional: any, val: any): any {
        if (val === null || typeof val !== "object" || Array.isArray(val)) {
            return invalidValue(l(ref || "object"), val, key, parent);
        }
        const result: any = {};
        Object.getOwnPropertyNames(props).forEach(key => {
            const prop = props[key];
            const v = Object.prototype.hasOwnProperty.call(val, key) ? val[key] : undefined;
            result[prop.key] = transform(v, prop.typ, getProps, key, ref);
        });
        Object.getOwnPropertyNames(val).forEach(key => {
            if (!Object.prototype.hasOwnProperty.call(props, key)) {
                result[key] = transform(val[key], additional, getProps, key, ref);
            }
        });
        return result;
    }

    if (typ === "any") return val;
    if (typ === null) {
        if (val === null) return val;
        return invalidValue(typ, val, key, parent);
    }
    if (typ === false) return invalidValue(typ, val, key, parent);
    let ref: any = undefined;
    while (typeof typ === "object" && typ.ref !== undefined) {
        ref = typ.ref;
        typ = typeMap[typ.ref];
    }
    if (Array.isArray(typ)) return transformEnum(typ, val);
    if (typeof typ === "object") {
        return typ.hasOwnProperty("unionMembers") ? transformUnion(typ.unionMembers, val)
            : typ.hasOwnProperty("arrayItems")    ? transformArray(typ.arrayItems, val)
            : typ.hasOwnProperty("props")         ? transformObject(getProps(typ), typ.additional, val)
            : invalidValue(typ, val, key, parent);
    }
    // Numbers can be parsed by Date but shouldn't be.
    if (typ === Date && typeof val !== "number") return transformDate(val);
    return transformPrimitive(typ, val);
}

function cast<T>(val: any, typ: any): T {
    return transform(val, typ, jsonToJSProps);
}

function uncast<T>(val: T, typ: any): any {
    return transform(val, typ, jsToJSONProps);
}

function l(typ: any) {
    return { literal: typ };
}

function a(typ: any) {
    return { arrayItems: typ };
}

function u(...typs: any[]) {
    return { unionMembers: typs };
}

function o(props: any[], additional: any) {
    return { props, additional };
}

function m(additional: any) {
    return { props: [], additional };
}

function r(name: string) {
    return { ref: name };
}

const typeMap: any = {
    "V211": o([
        { json: "cdr", js: "cdr", typ: u(undefined, r("Cdr")) },
        { json: "connector", js: "connector", typ: u(undefined, r("Connector")) },
        { json: "credentials", js: "credentials", typ: u(undefined, r("Credentials")) },
        { json: "evse", js: "evse", typ: u(undefined, r("Evse")) },
        { json: "location", js: "location", typ: u(undefined, r("Location")) },
        { json: "session", js: "session", typ: u(undefined, r("Session")) },
        { json: "tariff", js: "tariff", typ: u(undefined, r("Tariff")) },
        { json: "token", js: "token", typ: u(undefined, r("Token")) },
    ], "any"),
    "Cdr": o([
        { json: "auth_id", js: "auth_id", typ: "" },
        { json: "auth_method", js: "auth_method", typ: r("AuthMethod") },
        { json: "charging_periods", js: "charging_periods", typ: a(r("ChargingPeriod")) },
        { json: "currency", js: "currency", typ: "" },
        { json: "id", js: "id", typ: "" },
        { json: "last_updated", js: "last_updated", typ: "" },
        { json: "location", js: "location", typ: r("CdrLocation") },
        { json: "meter_id", js: "meter_id", typ: u(undefined, u(null, "")) },
        { json: "remark", js: "remark", typ: u(undefined, u(null, "")) },
        { json: "start_date_time", js: "start_date_time", typ: "" },
        { json: "stop_date_time", js: "stop_date_time", typ: "" },
        { json: "tariffs", js: "tariffs", typ: u(undefined, u(a(r("Tariff")), null)) },
        { json: "total_cost", js: "total_cost", typ: 3.14 },
        { json: "total_energy", js: "total_energy", typ: 3.14 },
        { json: "total_parking_time", js: "total_parking_time", typ: u(undefined, u(3.14, null)) },
        { json: "total_time", js: "total_time", typ: 3.14 },
    ], false),
    "ChargingPeriod": o([
        { json: "dimensions", js: "dimensions", typ: a(r("Dimension")) },
        { json: "start_date_time", js: "start_date_time", typ: "" },
    ], false),
    "Dimension": o([
        { json: "type", js: "type", typ: r("DimensionType") },
        { json: "volume", js: "volume", typ: 3.14 },
    ], false),
    "CdrLocation": o([
        { json: "id", js: "id", typ: "" },
        { json: "type", js: "type", typ: r("LocationType") },
        { json: "address", js: "address", typ: "" },
        { json: "city", js: "city", typ: "" },
        { json: "postal_code", js: "postal_code", typ: "" },
        { json: "country", js: "country", typ: "" },
        { json: "coordinates", js: "coordinates", typ: r("GeoLocation") },
        { json: "last_updated", js: "last_updated", typ: "" },
        { json: "charging_when_closed", js: "charging_when_closed", typ: u(undefined, u(true, null)) },
        { json: "directions", js: "directions", typ: u(undefined, u(a(r("DisplayText")), null)) },
        { json: "energy_mix", js: "energy_mix", typ: u(undefined, u(r("EnergyMix"), null)) },
        { json: "evses", js: "evses", typ: u(undefined, u(a(r("Evse")), null)) },
        { json: "facilities", js: "facilities", typ: u(undefined, u(a(r("Facility")), null)) },
        { json: "images", js: "images", typ: u(undefined, u(a(r("Image")), null)) },
        { json: "name", js: "name", typ: u(undefined, u(null, "")) },
        { json: "opening_times", js: "opening_times", typ: u(undefined, u(r("Hours"), null)) },
        { json: "operator", js: "operator", typ: u(undefined, u(r("BusinessDetails"), null)) },
        { json: "owner", js: "owner", typ: u(undefined, u(r("BusinessDetails"), null)) },
        { json: "related_locations", js: "related_locations", typ: u(undefined, u(a(r("RelatedLocation")), null)) },
        { json: "suboperator", js: "suboperator", typ: u(undefined, u(r("BusinessDetails"), null)) },
        { json: "time_zone", js: "time_zone", typ: u(undefined, u(null, "")) },
    ], false),
    "GeoLocation": o([
        { json: "latitude", js: "latitude", typ: u(undefined, "") },
        { json: "longitude", js: "longitude", typ: u(undefined, "") },
    ], false),
    "DisplayText": o([
        { json: "language", js: "language", typ: "" },
        { json: "text", js: "text", typ: "" },
    ], false),
    "EnergyMix": o([
        { json: "energy_product_name", js: "energy_product_name", typ: u(undefined, u(null, "")) },
        { json: "energy_sources", js: "energy_sources", typ: u(undefined, u(a(r("EnergySource")), null)) },
        { json: "environ_impact", js: "environ_impact", typ: u(undefined, u(a(r("EnvironImpact")), null)) },
        { json: "is_green_energy", js: "is_green_energy", typ: true },
        { json: "supplier_name", js: "supplier_name", typ: u(undefined, u(null, "")) },
    ], false),
    "EnergySource": o([
        { json: "percentage", js: "percentage", typ: 3.14 },
        { json: "source", js: "source", typ: r("EnergySourceSource") },
    ], false),
    "EnvironImpact": o([
        { json: "amount", js: "amount", typ: 3.14 },
        { json: "source", js: "source", typ: r("EnvironImpactSource") },
    ], false),
    "Evse": o([
        { json: "capabilities", js: "capabilities", typ: u(undefined, u(a(r("Capability")), null)) },
        { json: "connectors", js: "connectors", typ: u(undefined, a(r("Connector"))) },
        { json: "coordinates", js: "coordinates", typ: u(undefined, u(r("GeoLocation"), null)) },
        { json: "directions", js: "directions", typ: u(undefined, u(a(r("DisplayText")), null)) },
        { json: "evse_id", js: "evse_id", typ: u(undefined, u(null, "")) },
        { json: "floor_level", js: "floor_level", typ: u(undefined, u(null, "")) },
        { json: "images", js: "images", typ: u(undefined, u(a(r("Image")), null)) },
        { json: "last_updated", js: "last_updated", typ: u(undefined, "") },
        { json: "parking_restrictions", js: "parking_restrictions", typ: u(undefined, u(a(r("ParkingRestriction")), null)) },
        { json: "physical_reference", js: "physical_reference", typ: u(undefined, u(null, "")) },
        { json: "status", js: "status", typ: u(undefined, r("EvseStatus")) },
        { json: "status_schedule", js: "status_schedule", typ: u(undefined, u(a(r("StatusSchedule")), null)) },
        { json: "uid", js: "uid", typ: u(undefined, "") },
    ], false),
    "Connector": o([
        { json: "amperage", js: "amperage", typ: u(undefined, 0) },
        { json: "format", js: "format", typ: u(undefined, r("Format")) },
        { json: "id", js: "id", typ: u(undefined, "") },
        { json: "last_updated", js: "last_updated", typ: u(undefined, "") },
        { json: "power_type", js: "power_type", typ: u(undefined, r("PowerType")) },
        { json: "standard", js: "standard", typ: u(undefined, r("Standard")) },
        { json: "tariff_id", js: "tariff_id", typ: u(undefined, u(null, "")) },
        { json: "terms_and_conditions", js: "terms_and_conditions", typ: u(undefined, u(null, "")) },
        { json: "voltage", js: "voltage", typ: u(undefined, 0) },
    ], false),
    "Image": o([
        { json: "category", js: "category", typ: r("Category") },
        { json: "height", js: "height", typ: u(undefined, u(0, null)) },
        { json: "thumbnail", js: "thumbnail", typ: u(undefined, u(null, "")) },
        { json: "type", js: "type", typ: "" },
        { json: "url", js: "url", typ: "" },
        { json: "width", js: "width", typ: u(undefined, u(0, null)) },
    ], false),
    "StatusSchedule": o([
        { json: "period_begin", js: "period_begin", typ: "" },
        { json: "period_end", js: "period_end", typ: u(undefined, "") },
        { json: "status", js: "status", typ: r("EvseStatus") },
    ], false),
    "Hours": o([
        { json: "exceptional_closings", js: "exceptional_closings", typ: u(undefined, u(a(r("ExceptionalPeriod")), null)) },
        { json: "exceptional_openings", js: "exceptional_openings", typ: u(undefined, u(a(r("ExceptionalPeriod")), null)) },
        { json: "regular_hours", js: "regular_hours", typ: u(undefined, u(a(r("RegularHours")), null)) },
        { json: "twentyfourseven", js: "twentyfourseven", typ: u(undefined, true) },
    ], false),
    "ExceptionalPeriod": o([
        { json: "period_begin", js: "period_begin", typ: "" },
        { json: "period_end", js: "period_end", typ: "" },
    ], false),
    "RegularHours": o([
        { json: "period_begin", js: "period_begin", typ: u(undefined, "") },
        { json: "period_end", js: "period_end", typ: u(undefined, "") },
        { json: "weekday", js: "weekday", typ: u(undefined, 0) },
    ], false),
    "BusinessDetails": o([
        { json: "logo", js: "logo", typ: u(undefined, u(r("Image"), null)) },
        { json: "name", js: "name", typ: "" },
        { json: "website", js: "website", typ: u(undefined, u(null, "")) },
    ], false),
    "RelatedLocation": o([
        { json: "latitude", js: "latitude", typ: u(undefined, "") },
        { json: "longitude", js: "longitude", typ: u(undefined, "") },
        { json: "name", js: "name", typ: u(undefined, r("DisplayText")) },
    ], "any"),
    "Tariff": o([
        { json: "currency", js: "currency", typ: "" },
        { json: "elements", js: "elements", typ: a(r("TariffElement")) },
        { json: "energy_mix", js: "energy_mix", typ: u(undefined, u(r("EnergyMix"), null)) },
        { json: "id", js: "id", typ: "" },
        { json: "last_updated", js: "last_updated", typ: "" },
        { json: "tariff_alt_text", js: "tariff_alt_text", typ: u(undefined, u(a(r("DisplayText")), null)) },
        { json: "tariff_alt_url", js: "tariff_alt_url", typ: u(undefined, u(null, "")) },
    ], false),
    "TariffElement": o([
        { json: "price_components", js: "price_components", typ: a(r("PriceComponent")) },
        { json: "restrictions", js: "restrictions", typ: u(undefined, u(r("Restrictions"), null)) },
    ], false),
    "PriceComponent": o([
        { json: "price", js: "price", typ: 3.14 },
        { json: "step_size", js: "step_size", typ: 0 },
        { json: "type", js: "type", typ: r("PriceComponentType") },
    ], false),
    "Restrictions": o([
        { json: "day_of_week", js: "day_of_week", typ: u(undefined, u(a(r("DayOfWeek")), null)) },
        { json: "end_date", js: "end_date", typ: u(undefined, u(Date, null)) },
        { json: "end_time", js: "end_time", typ: u(undefined, u(null, "")) },
        { json: "max_duration", js: "max_duration", typ: u(undefined, u(0, null)) },
        { json: "max_kwh", js: "max_kwh", typ: u(undefined, u(3.14, null)) },
        { json: "max_power", js: "max_power", typ: u(undefined, u(3.14, null)) },
        { json: "min_duration", js: "min_duration", typ: u(undefined, u(0, null)) },
        { json: "min_kwh", js: "min_kwh", typ: u(undefined, u(3.14, null)) },
        { json: "min_power", js: "min_power", typ: u(undefined, u(3.14, null)) },
        { json: "start_date", js: "start_date", typ: u(undefined, u(Date, null)) },
        { json: "start_time", js: "start_time", typ: u(undefined, u(null, "")) },
    ], false),
    "Credentials": o([
        { json: "business_details", js: "business_details", typ: u(undefined, r("BusinessDetails")) },
        { json: "country_code", js: "country_code", typ: u(undefined, "") },
        { json: "party_id", js: "party_id", typ: u(undefined, "") },
        { json: "token", js: "token", typ: u(undefined, "") },
        { json: "url", js: "url", typ: u(undefined, "") },
    ], false),
    "Location": o([
        { json: "address", js: "address", typ: u(undefined, "") },
        { json: "charging_when_closed", js: "charging_when_closed", typ: u(undefined, u(true, null)) },
        { json: "city", js: "city", typ: u(undefined, "") },
        { json: "coordinates", js: "coordinates", typ: u(undefined, r("GeoLocation")) },
        { json: "country", js: "country", typ: u(undefined, "") },
        { json: "directions", js: "directions", typ: u(undefined, u(a(r("DisplayText")), null)) },
        { json: "energy_mix", js: "energy_mix", typ: u(undefined, u(r("EnergyMix"), null)) },
        { json: "evses", js: "evses", typ: u(undefined, u(a(r("Evse")), null)) },
        { json: "facilities", js: "facilities", typ: u(undefined, u(a(r("Facility")), null)) },
        { json: "id", js: "id", typ: u(undefined, "") },
        { json: "images", js: "images", typ: u(undefined, u(a(r("Image")), null)) },
        { json: "last_updated", js: "last_updated", typ: u(undefined, "") },
        { json: "name", js: "name", typ: u(undefined, u(null, "")) },
        { json: "opening_times", js: "opening_times", typ: u(undefined, u(r("Hours"), null)) },
        { json: "operator", js: "operator", typ: u(undefined, u(r("BusinessDetails"), null)) },
        { json: "owner", js: "owner", typ: u(undefined, u(r("BusinessDetails"), null)) },
        { json: "postal_code", js: "postal_code", typ: u(undefined, "") },
        { json: "related_locations", js: "related_locations", typ: u(undefined, u(a(r("RelatedLocation")), null)) },
        { json: "suboperator", js: "suboperator", typ: u(undefined, u(r("BusinessDetails"), null)) },
        { json: "time_zone", js: "time_zone", typ: u(undefined, u(null, "")) },
        { json: "type", js: "type", typ: u(undefined, r("LocationType")) },
    ], false),
    "Session": o([
        { json: "auth_id", js: "auth_id", typ: u(undefined, "") },
        { json: "auth_method", js: "auth_method", typ: u(undefined, r("AuthMethod")) },
        { json: "charging_periods", js: "charging_periods", typ: u(undefined, u(a(r("ChargingPeriod")), null)) },
        { json: "currency", js: "currency", typ: u(undefined, "") },
        { json: "end_datetime", js: "end_datetime", typ: u(undefined, u(null, "")) },
        { json: "id", js: "id", typ: u(undefined, "") },
        { json: "kwh", js: "kwh", typ: u(undefined, 3.14) },
        { json: "last_updated", js: "last_updated", typ: u(undefined, "") },
        { json: "location", js: "location", typ: u(undefined, r("SessionLocation")) },
        { json: "meter_id", js: "meter_id", typ: u(undefined, u(null, "")) },
        { json: "start_datetime", js: "start_datetime", typ: u(undefined, "") },
        { json: "status", js: "status", typ: u(undefined, r("Status")) },
        { json: "total_cost", js: "total_cost", typ: u(undefined, u(3.14, null)) },
    ], false),
    "SessionLocation": o([
        { json: "id", js: "id", typ: "" },
        { json: "type", js: "type", typ: r("LocationType") },
        { json: "address", js: "address", typ: "" },
        { json: "city", js: "city", typ: "" },
        { json: "postal_code", js: "postal_code", typ: "" },
        { json: "country", js: "country", typ: "" },
        { json: "coordinates", js: "coordinates", typ: r("GeoLocation") },
        { json: "last_updated", js: "last_updated", typ: "" },
        { json: "charging_when_closed", js: "charging_when_closed", typ: u(undefined, u(true, null)) },
        { json: "directions", js: "directions", typ: u(undefined, u(a(r("DisplayText")), null)) },
        { json: "energy_mix", js: "energy_mix", typ: u(undefined, u(r("EnergyMix"), null)) },
        { json: "evses", js: "evses", typ: u(undefined, u(a(r("Evse")), null)) },
        { json: "facilities", js: "facilities", typ: u(undefined, u(a(r("Facility")), null)) },
        { json: "images", js: "images", typ: u(undefined, u(a(r("Image")), null)) },
        { json: "name", js: "name", typ: u(undefined, u(null, "")) },
        { json: "opening_times", js: "opening_times", typ: u(undefined, u(r("Hours"), null)) },
        { json: "operator", js: "operator", typ: u(undefined, u(r("BusinessDetails"), null)) },
        { json: "owner", js: "owner", typ: u(undefined, u(r("BusinessDetails"), null)) },
        { json: "related_locations", js: "related_locations", typ: u(undefined, u(a(r("RelatedLocation")), null)) },
        { json: "suboperator", js: "suboperator", typ: u(undefined, u(r("BusinessDetails"), null)) },
        { json: "time_zone", js: "time_zone", typ: u(undefined, u(null, "")) },
    ], false),
    "Token": o([
        { json: "auth_id", js: "auth_id", typ: u(undefined, "") },
        { json: "issuer", js: "issuer", typ: u(undefined, "") },
        { json: "language", js: "language", typ: u(undefined, "") },
        { json: "last_updated", js: "last_updated", typ: u(undefined, "") },
        { json: "type", js: "type", typ: u(undefined, r("TokenType")) },
        { json: "uid", js: "uid", typ: u(undefined, "") },
        { json: "valid", js: "valid", typ: u(undefined, true) },
        { json: "visual_number", js: "visual_number", typ: u(undefined, "") },
        { json: "whitelist", js: "whitelist", typ: u(undefined, r("Whitelist")) },
    ], false),
    "AuthMethod": [
        "AUTH_REQUEST",
        "WHITELIST",
    ],
    "DimensionType": [
        "ENERGY",
        "FLAT",
        "MAX_CURRENT",
        "MIN_CURRENT",
        "PARKING_TIME",
        "TIME",
    ],
    "EnergySourceSource": [
        "COAL",
        "GAS",
        "GENERAL_FOSSIL",
        "GENERAL_GREEN",
        "NUCLEAR",
        "SOLAR",
        "WATER",
        "WIND",
    ],
    "EnvironImpactSource": [
        "CARBON_DIOXIDE",
        "NUCLEAR_WASTE",
    ],
    "Capability": [
        "CHARGING_PROFILE_CAPABLE",
        "CREDIT_CARD_PAYABLE",
        "RFID_READER",
        "REMOTE_START_STOP_CAPABLE",
        "RESERVABLE",
        "UNLOCK_CAPABLE",
    ],
    "Format": [
        "CABLE",
        "SOCKET",
    ],
    "PowerType": [
        "AC_1_PHASE",
        "AC_3_PHASE",
        "DC",
    ],
    "Standard": [
        "CHADEMO",
        "DOMESTIC_A",
        "DOMESTIC_B",
        "DOMESTIC_C",
        "DOMESTIC_D",
        "DOMESTIC_E",
        "DOMESTIC_F",
        "DOMESTIC_G",
        "DOMESTIC_H",
        "DOMESTIC_I",
        "DOMESTIC_J",
        "DOMESTIC_K",
        "DOMESTIC_L",
        "IEC_60309_2_single_16",
        "IEC_60309_2_three_16",
        "IEC_60309_2_three_32",
        "IEC_60309_2_three_64",
        "IEC_62196_T1",
        "IEC_62196_T1_COMBO",
        "IEC_62196_T2",
        "IEC_62196_T2_COMBO",
        "IEC_62196_T3A",
        "IEC_62196_T3C",
        "TESLA_R",
        "TESLA_S",
    ],
    "Category": [
        "CHARGER",
        "ENTRANCE",
        "LOCATION",
        "NETWORK",
        "OPERATOR",
        "OTHER",
        "OWNER",
    ],
    "ParkingRestriction": [
        "CUSTOMERS",
        "DISABLED",
        "EV_ONLY",
        "MOTORCYCLES",
        "PLUGGED",
    ],
    "EvseStatus": [
        "AVAILABLE",
        "BLOCKED",
        "CHARGING",
        "INOPERATIVE",
        "OUTOFORDER",
        "PLANNED",
        "REMOVED",
        "RESERVED",
        "UNKNOWN",
    ],
    "Facility": [
        "AIRPORT",
        "BUS_STOP",
        "CAFE",
        "CARPOOL_PARKING",
        "FUEL_STATION",
        "HOTEL",
        "MALL",
        "MUSEUM",
        "NATURE",
        "RECREATION_AREA",
        "RESTAURANT",
        "SPORT",
        "SUPERMARKET",
        "TAXI_STAND",
        "TRAIN_STATION",
        "WIFI",
    ],
    "LocationType": [
        "ON_STREET",
        "OTHER",
        "PARKING_GARAGE",
        "PARKING_LOT",
        "UNDERGROUND_GARAGE",
        "UNKNOWN",
    ],
    "PriceComponentType": [
        "ENERGY",
        "FLAT",
        "PARKING_TIME",
        "TIME",
    ],
    "DayOfWeek": [
        "FRIDAY",
        "MONDAY",
        "SATURDAY",
        "SUNDAY",
        "THURSDAY",
        "TUESDAY",
        "WEDNESDAY",
    ],
    "Status": [
        "ACTIVE",
        "COMPLETED",
        "INVALID",
        "PENDING",
    ],
    "TokenType": [
        "OTHER",
        "RFID",
    ],
    "Whitelist": [
        "ALLOWED",
        "ALLOWED_OFFLINE",
        "ALWAYS",
        "NEVER",
    ],
};
