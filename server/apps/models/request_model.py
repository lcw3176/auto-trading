from pydantic import BaseModel, field_validator


class Login(BaseModel):
    id: str
    pw: str

    @field_validator("id", "pw")
    def name_must_match_header(cls, v: str):
        if ' ' in v:
            raise ValueError('공백은 허용되지 않습니다')

        return v
