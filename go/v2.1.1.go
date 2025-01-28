// This file was generated from JSON Schema using quicktype, do not modify it directly.
// To parse and unparse this JSON data, add this code to your project and do:
//
//    v211, err := UnmarshalV211(bytes)
//    bytes, err = v211.Marshal()

package main

import "encoding/json"

func UnmarshalV211(data []byte) (V211, error) {
	var r V211
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *V211) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

type V211 struct {
	Cdr         *Cdr           `json:"cdr,omitempty"`
	Connector   *Connector     `json:"connector,omitempty"`
	Credentials *Credentials   `json:"credentials,omitempty"`
	Evse        *Evse          `json:"evse,omitempty"`
	Location    *V211_Location `json:"location,omitempty"`
	Session     *Session       `json:"session,omitempty"`
	Tariff      *Tariff        `json:"tariff,omitempty"`
	Token       *Token         `json:"token,omitempty"`
}

type Cdr struct {
	AuthID           string           `json:"auth_id"`
	AuthMethod       AuthMethod       `json:"auth_method"`
	ChargingPeriods  []ChargingPeriod `json:"charging_periods"`
	Currency         string           `json:"currency"`
	ID               string           `json:"id"`
	LastUpdated      string           `json:"last_updated"`
	Location         CdrLocation      `json:"location"`
	MeterID          *string          `json:"meter_id"`
	Remark           *string          `json:"remark"`
	StartDateTime    string           `json:"start_date_time"`
	StopDateTime     string           `json:"stop_date_time"`
	Tariffs          []Tariff         `json:"tariffs"`
	TotalCost        float64          `json:"total_cost"`
	TotalEnergy      float64          `json:"total_energy"`
	TotalParkingTime *float64         `json:"total_parking_time"`
	TotalTime        float64          `json:"total_time"`
}

type ChargingPeriod struct {
	Dimensions    []Dimension `json:"dimensions"`
	StartDateTime string      `json:"start_date_time"`
}

type Dimension struct {
	Type   DimensionType `json:"type"`
	Volume float64       `json:"volume"`
}

type CdrLocation struct {
	ID                 string            `json:"id"`
	Type               LocationType      `json:"type"`
	Address            string            `json:"address"`
	City               string            `json:"city"`
	PostalCode         string            `json:"postal_code"`
	Country            string            `json:"country"`
	Coordinates        GeoLocation       `json:"coordinates"`
	LastUpdated        string            `json:"last_updated"`
	ChargingWhenClosed *bool             `json:"charging_when_closed"`
	Directions         []DisplayText     `json:"directions"`
	EnergyMix          *EnergyMix        `json:"energy_mix"`
	Evses              []Evse            `json:"evses"`
	Facilities         []Facility        `json:"facilities"`
	Images             []Image           `json:"images"`
	Name               *string           `json:"name"`
	OpeningTimes       *Hours            `json:"opening_times"`
	Operator           *BusinessDetails  `json:"operator"`
	Owner              *BusinessDetails  `json:"owner"`
	RelatedLocations   []RelatedLocation `json:"related_locations"`
	Suboperator        *BusinessDetails  `json:"suboperator"`
	TimeZone           *string           `json:"time_zone"`
}

type GeoLocation struct {
	Latitude  *string `json:"latitude,omitempty"`
	Longitude *string `json:"longitude,omitempty"`
}

type DisplayText struct {
	Language string `json:"language"`
	Text     string `json:"text"`
}

type EnergyMix struct {
	EnergyProductName *string         `json:"energy_product_name"`
	EnergySources     []EnergySource  `json:"energy_sources"`
	EnvironImpact     []EnvironImpact `json:"environ_impact"`
	IsGreenEnergy     bool            `json:"is_green_energy"`
	SupplierName      *string         `json:"supplier_name"`
}

type EnergySource struct {
	Percentage float64            `json:"percentage"`
	Source     EnergySourceSource `json:"source"`
}

type EnvironImpact struct {
	Amount float64             `json:"amount"`
	Source EnvironImpactSource `json:"source"`
}

type Evse struct {
	Capabilities        []Capability         `json:"capabilities"`
	Connectors          []Connector          `json:"connectors,omitempty"`
	Coordinates         *GeoLocation         `json:"coordinates"`
	Directions          []DisplayText        `json:"directions"`
	EvseID              *string              `json:"evse_id"`
	FloorLevel          *string              `json:"floor_level"`
	Images              []Image              `json:"images"`
	LastUpdated         *string              `json:"last_updated,omitempty"`
	ParkingRestrictions []ParkingRestriction `json:"parking_restrictions"`
	PhysicalReference   *string              `json:"physical_reference"`
	Status              *EvseStatus          `json:"status,omitempty"`
	StatusSchedule      []StatusSchedule     `json:"status_schedule"`
	Uid                 *string              `json:"uid,omitempty"`
}

type Connector struct {
	Amperage           *int64     `json:"amperage,omitempty"`
	Format             *Format    `json:"format,omitempty"`
	ID                 *string    `json:"id,omitempty"`
	LastUpdated        *string    `json:"last_updated,omitempty"`
	PowerType          *PowerType `json:"power_type,omitempty"`
	Standard           *Standard  `json:"standard,omitempty"`
	TariffID           *string    `json:"tariff_id"`
	TermsAndConditions *string    `json:"terms_and_conditions"`
	Voltage            *int64     `json:"voltage,omitempty"`
}

type Image struct {
	Category  Category `json:"category"`
	Height    *int64   `json:"height"`
	Thumbnail *string  `json:"thumbnail"`
	Type      string   `json:"type"`
	URL       string   `json:"url"`
	Width     *int64   `json:"width"`
}

type StatusSchedule struct {
	PeriodBegin string     `json:"period_begin"`
	PeriodEnd   *string    `json:"period_end,omitempty"`
	Status      EvseStatus `json:"status"`
}

type Hours struct {
	ExceptionalClosings []ExceptionalPeriod `json:"exceptional_closings"`
	ExceptionalOpenings []ExceptionalPeriod `json:"exceptional_openings"`
	RegularHours        []RegularHours      `json:"regular_hours"`
	Twentyfourseven     *bool               `json:"twentyfourseven,omitempty"`
}

type ExceptionalPeriod struct {
	PeriodBegin string `json:"period_begin"`
	PeriodEnd   string `json:"period_end"`
}

type RegularHours struct {
	PeriodBegin *string `json:"period_begin,omitempty"`
	PeriodEnd   *string `json:"period_end,omitempty"`
	Weekday     *int64  `json:"weekday,omitempty"`
}

type BusinessDetails struct {
	Logo    *Image  `json:"logo"`
	Name    string  `json:"name"`
	Website *string `json:"website"`
}

type RelatedLocation struct {
	Latitude  *string      `json:"latitude,omitempty"`
	Longitude *string      `json:"longitude,omitempty"`
	Name      *DisplayText `json:"name,omitempty"`
}

type Tariff struct {
	Currency      string          `json:"currency"`
	Elements      []TariffElement `json:"elements"`
	EnergyMix     *EnergyMix      `json:"energy_mix"`
	ID            string          `json:"id"`
	LastUpdated   string          `json:"last_updated"`
	TariffAltText []DisplayText   `json:"tariff_alt_text"`
	TariffAltURL  *string         `json:"tariff_alt_url"`
}

type TariffElement struct {
	PriceComponents []PriceComponent `json:"price_components"`
	Restrictions    *Restrictions    `json:"restrictions"`
}

type PriceComponent struct {
	Price    float64            `json:"price"`
	StepSize int64              `json:"step_size"`
	Type     PriceComponentType `json:"type"`
}

type Restrictions struct {
	DayOfWeek   []DayOfWeek `json:"day_of_week"`
	EndDate     *string     `json:"end_date"`
	EndTime     *string     `json:"end_time"`
	MaxDuration *int64      `json:"max_duration"`
	MaxKwh      *float64    `json:"max_kwh"`
	MaxPower    *float64    `json:"max_power"`
	MinDuration *int64      `json:"min_duration"`
	MinKwh      *float64    `json:"min_kwh"`
	MinPower    *float64    `json:"min_power"`
	StartDate   *string     `json:"start_date"`
	StartTime   *string     `json:"start_time"`
}

type Credentials struct {
	BusinessDetails *BusinessDetails `json:"business_details,omitempty"`
	CountryCode     *string          `json:"country_code,omitempty"`
	PartyID         *string          `json:"party_id,omitempty"`
	Token           *string          `json:"token,omitempty"`
	URL             *string          `json:"url,omitempty"`
}

type V211_Location struct {
	Address            *string           `json:"address,omitempty"`
	ChargingWhenClosed *bool             `json:"charging_when_closed"`
	City               *string           `json:"city,omitempty"`
	Coordinates        *GeoLocation      `json:"coordinates,omitempty"`
	Country            *string           `json:"country,omitempty"`
	Directions         []DisplayText     `json:"directions"`
	EnergyMix          *EnergyMix        `json:"energy_mix"`
	Evses              []Evse            `json:"evses"`
	Facilities         []Facility        `json:"facilities"`
	ID                 *string           `json:"id,omitempty"`
	Images             []Image           `json:"images"`
	LastUpdated        *string           `json:"last_updated,omitempty"`
	Name               *string           `json:"name"`
	OpeningTimes       *Hours            `json:"opening_times"`
	Operator           *BusinessDetails  `json:"operator"`
	Owner              *BusinessDetails  `json:"owner"`
	PostalCode         *string           `json:"postal_code,omitempty"`
	RelatedLocations   []RelatedLocation `json:"related_locations"`
	Suboperator        *BusinessDetails  `json:"suboperator"`
	TimeZone           *string           `json:"time_zone"`
	Type               *LocationType     `json:"type,omitempty"`
}

type Session struct {
	AuthID          *string          `json:"auth_id,omitempty"`
	AuthMethod      *AuthMethod      `json:"auth_method,omitempty"`
	ChargingPeriods []ChargingPeriod `json:"charging_periods"`
	Currency        *string          `json:"currency,omitempty"`
	EndDatetime     *string          `json:"end_datetime"`
	ID              *string          `json:"id,omitempty"`
	Kwh             *float64         `json:"kwh,omitempty"`
	LastUpdated     *string          `json:"last_updated,omitempty"`
	Location        *SessionLocation `json:"location,omitempty"`
	MeterID         *string          `json:"meter_id"`
	StartDatetime   *string          `json:"start_datetime,omitempty"`
	Status          *Status          `json:"status,omitempty"`
	TotalCost       *float64         `json:"total_cost"`
}

type SessionLocation struct {
	ID                 string            `json:"id"`
	Type               LocationType      `json:"type"`
	Address            string            `json:"address"`
	City               string            `json:"city"`
	PostalCode         string            `json:"postal_code"`
	Country            string            `json:"country"`
	Coordinates        GeoLocation       `json:"coordinates"`
	LastUpdated        string            `json:"last_updated"`
	ChargingWhenClosed *bool             `json:"charging_when_closed"`
	Directions         []DisplayText     `json:"directions"`
	EnergyMix          *EnergyMix        `json:"energy_mix"`
	Evses              []Evse            `json:"evses"`
	Facilities         []Facility        `json:"facilities"`
	Images             []Image           `json:"images"`
	Name               *string           `json:"name"`
	OpeningTimes       *Hours            `json:"opening_times"`
	Operator           *BusinessDetails  `json:"operator"`
	Owner              *BusinessDetails  `json:"owner"`
	RelatedLocations   []RelatedLocation `json:"related_locations"`
	Suboperator        *BusinessDetails  `json:"suboperator"`
	TimeZone           *string           `json:"time_zone"`
}

type Token struct {
	AuthID       *string        `json:"auth_id,omitempty"`
	Issuer       *string        `json:"issuer,omitempty"`
	Language     *string        `json:"language,omitempty"`
	LastUpdated  *string        `json:"last_updated,omitempty"`
	Type         *TokenType     `json:"type,omitempty"`
	Uid          *string        `json:"uid,omitempty"`
	Valid        *bool          `json:"valid,omitempty"`
	VisualNumber *string        `json:"visual_number,omitempty"`
	Whitelist    *WhitelistEnum `json:"whitelist,omitempty"`
}

type AuthMethod string

const (
	AuthRequest AuthMethod = "AUTH_REQUEST"
	Whitelist   AuthMethod = "WHITELIST"
)

type DimensionType string

const (
	MaxCurrent        DimensionType = "MAX_CURRENT"
	MinCurrent        DimensionType = "MIN_CURRENT"
	PurpleENERGY      DimensionType = "ENERGY"
	PurpleFLAT        DimensionType = "FLAT"
	PurplePARKINGTIME DimensionType = "PARKING_TIME"
	PurpleTIME        DimensionType = "TIME"
)

type EnergySourceSource string

const (
	Coal          EnergySourceSource = "COAL"
	Gas           EnergySourceSource = "GAS"
	GeneralFossil EnergySourceSource = "GENERAL_FOSSIL"
	GeneralGreen  EnergySourceSource = "GENERAL_GREEN"
	Nuclear       EnergySourceSource = "NUCLEAR"
	Solar         EnergySourceSource = "SOLAR"
	Water         EnergySourceSource = "WATER"
	Wind          EnergySourceSource = "WIND"
)

type EnvironImpactSource string

const (
	CarbonDioxide EnvironImpactSource = "CARBON_DIOXIDE"
	NuclearWaste  EnvironImpactSource = "NUCLEAR_WASTE"
)

type Capability string

const (
	ChargingProfileCapable Capability = "CHARGING_PROFILE_CAPABLE"
	CreditCardPayable      Capability = "CREDIT_CARD_PAYABLE"
	RFIDReader             Capability = "RFID_READER"
	RemoteStartStopCapable Capability = "REMOTE_START_STOP_CAPABLE"
	Reservable             Capability = "RESERVABLE"
	UnlockCapable          Capability = "UNLOCK_CAPABLE"
)

type Format string

const (
	Cable  Format = "CABLE"
	Socket Format = "SOCKET"
)

type PowerType string

const (
	AC1_Phase PowerType = "AC_1_PHASE"
	AC3_Phase PowerType = "AC_3_PHASE"
	Dc        PowerType = "DC"
)

type Standard string

const (
	Chademo             Standard = "CHADEMO"
	DomesticA           Standard = "DOMESTIC_A"
	DomesticB           Standard = "DOMESTIC_B"
	DomesticC           Standard = "DOMESTIC_C"
	DomesticD           Standard = "DOMESTIC_D"
	DomesticE           Standard = "DOMESTIC_E"
	DomesticF           Standard = "DOMESTIC_F"
	DomesticG           Standard = "DOMESTIC_G"
	DomesticH           Standard = "DOMESTIC_H"
	DomesticI           Standard = "DOMESTIC_I"
	DomesticJ           Standard = "DOMESTIC_J"
	DomesticK           Standard = "DOMESTIC_K"
	DomesticL           Standard = "DOMESTIC_L"
	IEC60309_2_Single16 Standard = "IEC_60309_2_single_16"
	IEC60309_2_Three16  Standard = "IEC_60309_2_three_16"
	IEC60309_2_Three32  Standard = "IEC_60309_2_three_32"
	IEC60309_2_Three64  Standard = "IEC_60309_2_three_64"
	IEC62196_T1         Standard = "IEC_62196_T1"
	IEC62196_T1Combo    Standard = "IEC_62196_T1_COMBO"
	IEC62196_T2         Standard = "IEC_62196_T2"
	IEC62196_T2Combo    Standard = "IEC_62196_T2_COMBO"
	IEC62196_T3A        Standard = "IEC_62196_T3A"
	IEC62196_T3C        Standard = "IEC_62196_T3C"
	TeslaR              Standard = "TESLA_R"
	TeslaS              Standard = "TESLA_S"
)

type Category string

const (
	CategoryOTHER Category = "OTHER"
	Charger       Category = "CHARGER"
	Entrance      Category = "ENTRANCE"
	Location      Category = "LOCATION"
	Network       Category = "NETWORK"
	Operator      Category = "OPERATOR"
	Owner         Category = "OWNER"
)

type ParkingRestriction string

const (
	Customers   ParkingRestriction = "CUSTOMERS"
	Disabled    ParkingRestriction = "DISABLED"
	EvOnly      ParkingRestriction = "EV_ONLY"
	Motorcycles ParkingRestriction = "MOTORCYCLES"
	Plugged     ParkingRestriction = "PLUGGED"
)

type EvseStatus string

const (
	Available         EvseStatus = "AVAILABLE"
	Blocked           EvseStatus = "BLOCKED"
	Charging          EvseStatus = "CHARGING"
	EvseStatusUNKNOWN EvseStatus = "UNKNOWN"
	Inoperative       EvseStatus = "INOPERATIVE"
	Outoforder        EvseStatus = "OUTOFORDER"
	Planned           EvseStatus = "PLANNED"
	Removed           EvseStatus = "REMOVED"
	Reserved          EvseStatus = "RESERVED"
)

type Facility string

const (
	Airport        Facility = "AIRPORT"
	BusStop        Facility = "BUS_STOP"
	Cafe           Facility = "CAFE"
	CarpoolParking Facility = "CARPOOL_PARKING"
	FuelStation    Facility = "FUEL_STATION"
	Hotel          Facility = "HOTEL"
	Mall           Facility = "MALL"
	Museum         Facility = "MUSEUM"
	Nature         Facility = "NATURE"
	RecreationArea Facility = "RECREATION_AREA"
	Restaurant     Facility = "RESTAURANT"
	Sport          Facility = "SPORT"
	Supermarket    Facility = "SUPERMARKET"
	TaxiStand      Facility = "TAXI_STAND"
	TrainStation   Facility = "TRAIN_STATION"
	Wifi           Facility = "WIFI"
)

type LocationType string

const (
	OnStreet          LocationType = "ON_STREET"
	ParkingGarage     LocationType = "PARKING_GARAGE"
	ParkingLot        LocationType = "PARKING_LOT"
	PurpleOTHER       LocationType = "OTHER"
	TypeUNKNOWN       LocationType = "UNKNOWN"
	UndergroundGarage LocationType = "UNDERGROUND_GARAGE"
)

type PriceComponentType string

const (
	FluffyENERGY      PriceComponentType = "ENERGY"
	FluffyFLAT        PriceComponentType = "FLAT"
	FluffyPARKINGTIME PriceComponentType = "PARKING_TIME"
	FluffyTIME        PriceComponentType = "TIME"
)

type DayOfWeek string

const (
	Friday    DayOfWeek = "FRIDAY"
	Monday    DayOfWeek = "MONDAY"
	Saturday  DayOfWeek = "SATURDAY"
	Sunday    DayOfWeek = "SUNDAY"
	Thursday  DayOfWeek = "THURSDAY"
	Tuesday   DayOfWeek = "TUESDAY"
	Wednesday DayOfWeek = "WEDNESDAY"
)

type Status string

const (
	Active    Status = "ACTIVE"
	Completed Status = "COMPLETED"
	Invalid   Status = "INVALID"
	Pending   Status = "PENDING"
)

type TokenType string

const (
	FluffyOTHER TokenType = "OTHER"
	RFID        TokenType = "RFID"
)

type WhitelistEnum string

const (
	Allowed        WhitelistEnum = "ALLOWED"
	AllowedOffline WhitelistEnum = "ALLOWED_OFFLINE"
	Always         WhitelistEnum = "ALWAYS"
	Never          WhitelistEnum = "NEVER"
)
