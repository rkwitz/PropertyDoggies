import dash_bootstrap_components as dbc

navbar = dbc.Navbar(
    children=[
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    dbc.NavbarBrand(dbc.NavLink("Property Doggies", href="/")),
                ],
                    width={"size": "auto"})
            ],
                align="center",
                className="g-0"),
            dbc.NavItem(dbc.NavLink("Map", href="/map")),
            dbc.NavItem(dbc.NavLink("Data", href="/data")),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("Time Series", header=True),
                    dbc.DropdownMenuItem("Page 2", href="#"),
                    dbc.DropdownMenuItem("Page 3", href="#"),
                ],
                nav=True,
                in_navbar=True,
                label="EDA",
            ),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("Export", header=True),
                    dbc.DropdownMenuItem("Bio", href="/bio"),
                    dbc.DropdownMenuItem("Photos", href="/myphotos"),
                ],
                nav=True,
                in_navbar=True,
                label="Export",
            ),
        ])
    ],
    color="primary",
    dark=True,
    sticky="top"
)
