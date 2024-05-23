// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::v2.1.1;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: v2.1.1 = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize)]
pub struct V211 {
    cdr: Option<Cdr>,

    connector: Option<Connector>,

    credentials: Option<Credentials>,

    evse: Option<Evse>,

    location: Option<Location>,

    session: Option<Session>,

    tariff: Option<Tariff>,

    token: Option<Token>,
}

#[derive(Serialize, Deserialize)]
pub struct Cdr {
    auth_id: String,

    auth_method: AuthMethod,

    charging_periods: Vec<ChargingPeriod>,

    currency: String,

    id: String,

    last_updated: String,

    location: CdrLocation,

    meter_id: Option<String>,

    remark: Option<String>,

    start_date_time: String,

    stop_date_time: String,

    tariffs: Option<Vec<Tariff>>,

    total_cost: f64,

    total_energy: f64,

    total_parking_time: Option<f64>,

    total_time: f64,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum AuthMethod {
    #[serde(rename = "AUTH_REQUEST")]
    AuthRequest,

    Whitelist,
}

#[derive(Serialize, Deserialize)]
pub struct ChargingPeriod {
    dimensions: Vec<Dimension>,

    start_date_time: String,
}

#[derive(Serialize, Deserialize)]
pub struct Dimension {
    #[serde(rename = "type")]
    dimension_type: DimensionType,

    volume: f64,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum DimensionType {
    Energy,

    Flat,

    #[serde(rename = "MAX_CURRENT")]
    MaxCurrent,

    #[serde(rename = "MIN_CURRENT")]
    MinCurrent,

    #[serde(rename = "PARKING_TIME")]
    ParkingTime,

    Time,
}

#[derive(Serialize, Deserialize)]
pub struct CdrLocation {
    id: String,

    #[serde(rename = "type")]
    location_type: LocationType,

    address: String,

    city: String,

    postal_code: String,

    country: String,

    coordinates: GeoLocation,

    last_updated: String,

    charging_when_closed: Option<bool>,

    directions: Option<Vec<DisplayText>>,

    energy_mix: Option<EnergyMix>,

    evses: Option<Vec<Evse>>,

    facilities: Option<Vec<Facility>>,

    images: Option<Vec<Image>>,

    name: Option<String>,

    opening_times: Option<Hours>,

    operator: Option<BusinessDetails>,

    owner: Option<BusinessDetails>,

    related_locations: Option<Vec<RelatedLocation>>,

    suboperator: Option<BusinessDetails>,

    time_zone: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub struct GeoLocation {
    latitude: Option<String>,

    longitude: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub struct DisplayText {
    language: String,

    text: String,
}

#[derive(Serialize, Deserialize)]
pub struct EnergyMix {
    energy_product_name: Option<String>,

    energy_sources: Option<Vec<EnergySource>>,

    environ_impact: Option<Vec<EnvironImpact>>,

    is_green_energy: bool,

    supplier_name: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub struct EnergySource {
    percentage: f64,

    source: EnergySourceSource,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum EnergySourceSource {
    Coal,

    Gas,

    #[serde(rename = "GENERAL_FOSSIL")]
    GeneralFossil,

    #[serde(rename = "GENERAL_GREEN")]
    GeneralGreen,

    Nuclear,

    Solar,

    Water,

    Wind,
}

#[derive(Serialize, Deserialize)]
pub struct EnvironImpact {
    amount: f64,

    source: EnvironImpactSource,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum EnvironImpactSource {
    #[serde(rename = "CARBON_DIOXIDE")]
    CarbonDioxide,

    #[serde(rename = "NUCLEAR_WASTE")]
    NuclearWaste,
}

#[derive(Serialize, Deserialize)]
pub struct Evse {
    capabilities: Option<Vec<Capability>>,

    connectors: Option<Vec<Connector>>,

    coordinates: Option<GeoLocation>,

    directions: Option<Vec<DisplayText>>,

    evse_id: Option<String>,

    floor_level: Option<String>,

    images: Option<Vec<Image>>,

    last_updated: Option<String>,

    parking_restrictions: Option<Vec<ParkingRestriction>>,

    physical_reference: Option<String>,

    status: Option<EvseStatus>,

    status_schedule: Option<Vec<StatusSchedule>>,

    uid: Option<String>,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum Capability {
    #[serde(rename = "CHARGING_PROFILE_CAPABLE")]
    ChargingProfileCapable,

    #[serde(rename = "CREDIT_CARD_PAYABLE")]
    CreditCardPayable,

    #[serde(rename = "REMOTE_START_STOP_CAPABLE")]
    RemoteStartStopCapable,

    Reservable,

    #[serde(rename = "RFID_READER")]
    RfidReader,

    #[serde(rename = "UNLOCK_CAPABLE")]
    UnlockCapable,
}

#[derive(Serialize, Deserialize)]
pub struct Connector {
    amperage: Option<i64>,

    format: Option<Format>,

    id: Option<String>,

    last_updated: Option<String>,

    power_type: Option<PowerType>,

    standard: Option<Standard>,

    tariff_id: Option<String>,

    terms_and_conditions: Option<String>,

    voltage: Option<i64>,
}

#[derive(Serialize, Deserialize)]
pub enum Format {
    #[serde(rename = "CABLE")]
    Cable,

    #[serde(rename = "SOCKET")]
    Socket,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum PowerType {
    #[serde(rename = "AC_1_PHASE")]
    Ac1_Phase,

    #[serde(rename = "AC_3_PHASE")]
    Ac3_Phase,

    Dc,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum Standard {
    Chademo,

    #[serde(rename = "DOMESTIC_A")]
    DomesticA,

    #[serde(rename = "DOMESTIC_B")]
    DomesticB,

    #[serde(rename = "DOMESTIC_C")]
    DomesticC,

    #[serde(rename = "DOMESTIC_D")]
    DomesticD,

    #[serde(rename = "DOMESTIC_E")]
    DomesticE,

    #[serde(rename = "DOMESTIC_F")]
    DomesticF,

    #[serde(rename = "DOMESTIC_G")]
    DomesticG,

    #[serde(rename = "DOMESTIC_H")]
    DomesticH,

    #[serde(rename = "DOMESTIC_I")]
    DomesticI,

    #[serde(rename = "DOMESTIC_J")]
    DomesticJ,

    #[serde(rename = "DOMESTIC_K")]
    DomesticK,

    #[serde(rename = "DOMESTIC_L")]
    DomesticL,

    #[serde(rename = "IEC_60309_2_single_16")]
    Iec60309_2_Single16,

    #[serde(rename = "IEC_60309_2_three_16")]
    Iec60309_2_Three16,

    #[serde(rename = "IEC_60309_2_three_32")]
    Iec60309_2_Three32,

    #[serde(rename = "IEC_60309_2_three_64")]
    Iec60309_2_Three64,

    #[serde(rename = "IEC_62196_T1")]
    Iec62196_T1,

    #[serde(rename = "IEC_62196_T1_COMBO")]
    Iec62196_T1Combo,

    #[serde(rename = "IEC_62196_T2")]
    Iec62196_T2,

    #[serde(rename = "IEC_62196_T2_COMBO")]
    Iec62196_T2Combo,

    #[serde(rename = "IEC_62196_T3A")]
    Iec62196_T3A,

    #[serde(rename = "IEC_62196_T3C")]
    Iec62196_T3C,

    #[serde(rename = "TESLA_R")]
    TeslaR,

    #[serde(rename = "TESLA_S")]
    TeslaS,
}

#[derive(Serialize, Deserialize)]
pub struct Image {
    category: Category,

    height: Option<i64>,

    thumbnail: Option<String>,

    #[serde(rename = "type")]
    image_type: String,

    url: String,

    width: Option<i64>,
}

#[derive(Serialize, Deserialize)]
pub enum Category {
    #[serde(rename = "CHARGER")]
    Charger,

    #[serde(rename = "ENTRANCE")]
    Entrance,

    #[serde(rename = "LOCATION")]
    Location,

    #[serde(rename = "NETWORK")]
    Network,

    #[serde(rename = "OPERATOR")]
    Operator,

    #[serde(rename = "OTHER")]
    Other,

    #[serde(rename = "OWNER")]
    Owner,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum ParkingRestriction {
    Customers,

    Disabled,

    #[serde(rename = "EV_ONLY")]
    EvOnly,

    Motorcycles,

    Plugged,
}

#[derive(Serialize, Deserialize)]
pub enum EvseStatus {
    #[serde(rename = "AVAILABLE")]
    Available,

    #[serde(rename = "BLOCKED")]
    Blocked,

    #[serde(rename = "CHARGING")]
    Charging,

    #[serde(rename = "INOPERATIVE")]
    Inoperative,

    #[serde(rename = "OUTOFORDER")]
    Outoforder,

    #[serde(rename = "PLANNED")]
    Planned,

    #[serde(rename = "REMOVED")]
    Removed,

    #[serde(rename = "RESERVED")]
    Reserved,

    #[serde(rename = "UNKNOWN")]
    Unknown,
}

#[derive(Serialize, Deserialize)]
pub struct StatusSchedule {
    period_begin: String,

    period_end: Option<String>,

    status: EvseStatus,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum Facility {
    Airport,

    #[serde(rename = "BUS_STOP")]
    BusStop,

    Cafe,

    #[serde(rename = "CARPOOL_PARKING")]
    CarpoolParking,

    #[serde(rename = "FUEL_STATION")]
    FuelStation,

    Hotel,

    Mall,

    Museum,

    Nature,

    #[serde(rename = "RECREATION_AREA")]
    RecreationArea,

    Restaurant,

    Sport,

    Supermarket,

    #[serde(rename = "TAXI_STAND")]
    TaxiStand,

    #[serde(rename = "TRAIN_STATION")]
    TrainStation,

    Wifi,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum LocationType {
    #[serde(rename = "ON_STREET")]
    OnStreet,

    Other,

    #[serde(rename = "PARKING_GARAGE")]
    ParkingGarage,

    #[serde(rename = "PARKING_LOT")]
    ParkingLot,

    #[serde(rename = "UNDERGROUND_GARAGE")]
    UndergroundGarage,

    Unknown,
}

#[derive(Serialize, Deserialize)]
pub struct Hours {
    exceptional_closings: Option<Vec<ExceptionalPeriod>>,

    exceptional_openings: Option<Vec<ExceptionalPeriod>>,

    regular_hours: Option<Vec<RegularHours>>,

    twentyfourseven: Option<bool>,
}

#[derive(Serialize, Deserialize)]
pub struct ExceptionalPeriod {
    period_begin: String,

    period_end: String,
}

#[derive(Serialize, Deserialize)]
pub struct RegularHours {
    period_begin: Option<String>,

    period_end: Option<String>,

    weekday: Option<i64>,
}

#[derive(Serialize, Deserialize)]
pub struct BusinessDetails {
    logo: Option<Image>,

    name: String,

    website: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub struct RelatedLocation {
    latitude: Option<String>,

    longitude: Option<String>,

    name: Option<DisplayText>,
}

#[derive(Serialize, Deserialize)]
pub struct Tariff {
    currency: String,

    elements: Vec<TariffElement>,

    energy_mix: Option<EnergyMix>,

    id: String,

    last_updated: String,

    tariff_alt_text: Option<Vec<DisplayText>>,

    tariff_alt_url: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub struct TariffElement {
    price_components: Vec<PriceComponent>,

    restrictions: Option<Restrictions>,
}

#[derive(Serialize, Deserialize)]
pub struct PriceComponent {
    price: f64,

    step_size: i64,

    #[serde(rename = "type")]
    price_component_type: PriceComponentType,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum PriceComponentType {
    Energy,

    Flat,

    #[serde(rename = "PARKING_TIME")]
    ParkingTime,

    Time,
}

#[derive(Serialize, Deserialize)]
pub struct Restrictions {
    day_of_week: Option<Vec<DayOfWeek>>,

    end_date: Option<String>,

    end_time: Option<String>,

    max_duration: Option<i64>,

    max_kwh: Option<f64>,

    max_power: Option<f64>,

    min_duration: Option<i64>,

    min_kwh: Option<f64>,

    min_power: Option<f64>,

    start_date: Option<String>,

    start_time: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub enum DayOfWeek {
    #[serde(rename = "FRIDAY")]
    Friday,

    #[serde(rename = "MONDAY")]
    Monday,

    #[serde(rename = "SATURDAY")]
    Saturday,

    #[serde(rename = "SUNDAY")]
    Sunday,

    #[serde(rename = "THURSDAY")]
    Thursday,

    #[serde(rename = "TUESDAY")]
    Tuesday,

    #[serde(rename = "WEDNESDAY")]
    Wednesday,
}

#[derive(Serialize, Deserialize)]
pub struct Credentials {
    business_details: Option<BusinessDetails>,

    country_code: Option<String>,

    party_id: Option<String>,

    token: Option<String>,

    url: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub struct Location {
    address: Option<String>,

    charging_when_closed: Option<bool>,

    city: Option<String>,

    coordinates: Option<GeoLocation>,

    country: Option<String>,

    directions: Option<Vec<DisplayText>>,

    energy_mix: Option<EnergyMix>,

    evses: Option<Vec<Evse>>,

    facilities: Option<Vec<Facility>>,

    id: Option<String>,

    images: Option<Vec<Image>>,

    last_updated: Option<String>,

    name: Option<String>,

    opening_times: Option<Hours>,

    operator: Option<BusinessDetails>,

    owner: Option<BusinessDetails>,

    postal_code: Option<String>,

    related_locations: Option<Vec<RelatedLocation>>,

    suboperator: Option<BusinessDetails>,

    time_zone: Option<String>,

    #[serde(rename = "type")]
    location_type: Option<LocationType>,
}

#[derive(Serialize, Deserialize)]
pub struct Session {
    auth_id: Option<String>,

    auth_method: Option<AuthMethod>,

    charging_periods: Option<Vec<ChargingPeriod>>,

    currency: Option<String>,

    end_datetime: Option<String>,

    id: Option<String>,

    kwh: Option<f64>,

    last_updated: Option<String>,

    location: Option<SessionLocation>,

    meter_id: Option<String>,

    start_datetime: Option<String>,

    status: Option<Status>,

    total_cost: Option<f64>,
}

#[derive(Serialize, Deserialize)]
pub struct SessionLocation {
    id: String,

    #[serde(rename = "type")]
    location_type: LocationType,

    address: String,

    city: String,

    postal_code: String,

    country: String,

    coordinates: GeoLocation,

    last_updated: String,

    charging_when_closed: Option<bool>,

    directions: Option<Vec<DisplayText>>,

    energy_mix: Option<EnergyMix>,

    evses: Option<Vec<Evse>>,

    facilities: Option<Vec<Facility>>,

    images: Option<Vec<Image>>,

    name: Option<String>,

    opening_times: Option<Hours>,

    operator: Option<BusinessDetails>,

    owner: Option<BusinessDetails>,

    related_locations: Option<Vec<RelatedLocation>>,

    suboperator: Option<BusinessDetails>,

    time_zone: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub enum Status {
    #[serde(rename = "ACTIVE")]
    Active,

    #[serde(rename = "COMPLETED")]
    Completed,

    #[serde(rename = "INVALID")]
    Invalid,

    #[serde(rename = "PENDING")]
    Pending,
}

#[derive(Serialize, Deserialize)]
pub struct Token {
    auth_id: Option<String>,

    issuer: Option<String>,

    language: Option<String>,

    last_updated: Option<String>,

    #[serde(rename = "type")]
    token_type: Option<TokenType>,

    uid: Option<String>,

    valid: Option<bool>,

    visual_number: Option<String>,

    whitelist: Option<Whitelist>,
}

#[derive(Serialize, Deserialize)]
pub enum TokenType {
    #[serde(rename = "OTHER")]
    Other,

    #[serde(rename = "RFID")]
    Rfid,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum Whitelist {
    Allowed,

    #[serde(rename = "ALLOWED_OFFLINE")]
    AllowedOffline,

    Always,

    Never,
}
