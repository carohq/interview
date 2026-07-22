import json
import os
from typing import TypedDict, Literal, Optional

HeadcountStatus = Literal['in_seat', 'pending_term', 'pending_start']


class Headcount(TypedDict):
    id: str
    name: str
    status: HeadcountStatus
    costCenterId: str


class CostCenter(TypedDict):
    id: str
    name: str
    parentId: Optional[str]


class Database:
    def __init__(self):
        self._headcount_data: list[Headcount] = self._load_json('headcount.json')
        self._cost_centers_data: list[CostCenter] = self._load_json('cost-centers.json')

    def _load_json(self, filename: str) -> list:
        data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
        file_path = os.path.join(data_dir, filename)
        with open(file_path, 'r') as f:
            return json.load(f)

    def get_headcount(self) -> list[Headcount]:
        """Get all headcount records"""
        return self._headcount_data

    def get_headcount_by_id(self, id: str) -> Optional[Headcount]:
        """Get a specific headcount record by ID"""
        return next((hc for hc in self._headcount_data if hc['id'] == id), None)

    def get_cost_centers(self) -> list[CostCenter]:
        """Get all cost centers"""
        return self._cost_centers_data

    def get_cost_center_by_id(self, id: str) -> Optional[CostCenter]:
        """Get a specific cost center by ID"""
        return next((cc for cc in self._cost_centers_data if cc['id'] == id), None)
