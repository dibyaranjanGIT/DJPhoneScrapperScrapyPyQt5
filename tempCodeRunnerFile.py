def initUI(self):
        main_widget = GradientWidget()
        main_layout = QHBoxLayout(main_widget)  # Main layout is horizontal

        # Table layout on the left side
        table_layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels(["Sl.", "🌐 Website", "Phone Number 1️⃣", "🗺️ Country", "Phone Number 2️⃣", "🗺️ Country", "Phone Number 3️⃣", "🗺️ Country"])

        # Set custom stylesheet for header
        self.table.setStyleSheet("""
            QHeaderView::section {
                background-color: #E6E6FA;
                color: black;
                padding: 4px;
                border: 1px solid lightgray;
                font-family: "Core Sans DS 45 Medium";
            }
        """)

        # Hide the vertical header to remove the default row numbers
        self.table.verticalHeader().setVisible(False)

        # Allow manual resizing of columns
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Interactive)  # Allow manual resizing
        header.setStretchLastSection(True)  # Stretch last section to fill the available space

        table_layout.addWidget(self.table)

        # Controls layout on the right side
        controls_layout = QVBoxLayout()

        # Define the custom stylesheet for buttons
        button_stylesheet = """
        QPushButton {
            background-color: #ffffff; 
            color: black;
            border: 1px solid lightgray;
            border-radius: 15px; 
            padding: 8px;
            font-family: "Core Sans DS 45 Medium";
            font-size: 15px;
        }
        QPushButton:hover {
            background-color: #D8BFD8;
        }
        QPushButton:pressed {
            background-color: #2846ca;
        }
        """

        save_csv_button_stylesheet = """
        QPushButton {
            background-color: #ffffff; 
            color: green;
            border: 1px solid black;
            border-radius: 15px; 
            padding: 6px;
            font-family: "Core Sans DS 45 Medium";
            font-size: 15px;
        }
        QPushButton:hover {
            background-color: #D8BFD8;
        }
        QPushButton:pressed {
            background-color: #2846ca;
        }
        """

        save_excel_button_stylesheet = """
        QPushButton {
            background-color: #ffffff; 
            color: purple;
            border: 1px solid black;
            border-radius: 15px; 
            padding: 6px;
            font-family: "Core Sans DS 45 Medium";
            font-size: 15px;
        }
        QPushButton:hover {
            background-color: #D8BFD8;
        }
        QPushButton:pressed {
            background-color: #2846ca;
        }
        """
        single_button_stylesheet = """
        QPushButton {
            background-color: #ffffff; 
            color: black;
            border: 1px solid lightgray;
            border-radius: 15px; 
            padding: 8px;
            font-family: "Core Sans DS 45 Medium";
            font-size: 15px;
        }
        QPushButton:hover {
            background-color: #D8BFD8;
        }
        QPushButton:pressed {
            background-color: #2846ca;
        }
        """

        # Top row buttons layout
        top_buttons_layout = QHBoxLayout()

        self.start_button = QPushButton("▶️ Start")
        self.start_button.setFixedSize(140, 40)
        self.start_button.setStyleSheet(button_stylesheet)
        self.start_button.clicked.connect(self.start_scraping)
        top_buttons_layout.addWidget(self.start_button)

        # Add a horizontal spacer to increase space between top buttons and browse button
        horizontal_spacer_top = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        top_buttons_layout.addItem(horizontal_spacer_top)

        self.stop_button = QPushButton("⛔ Stop")
        self.stop_button.setFixedSize(140, 40)
        self.stop_button.setStyleSheet(button_stylesheet)
        self.stop_button.clicked.connect(self.stop_scraping)
        top_buttons_layout.addWidget(self.stop_button)

        # Add a horizontal spacer to increase space between top buttons and browse button
        horizontal_spacer_top1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        top_buttons_layout.addItem(horizontal_spacer_top1)

        self.clear_button = QPushButton("❌ Clear")
        self.clear_button.setFixedSize(140, 40)
        self.clear_button.setStyleSheet(button_stylesheet)
        self.clear_button.clicked.connect(self.clear_results)
        top_buttons_layout.addWidget(self.clear_button)

        # Add a spacer to push buttons to the left
        top_buttons_layout.addStretch(1)

        controls_layout.addLayout(top_buttons_layout)

        # Add a vertical spacer to increase space between top buttons and browse button
        vertical_spacer_top = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)
        controls_layout.addItem(vertical_spacer_top)

        # Second row buttons layout
        second_buttons_layout = QHBoxLayout()

        self.pause_button = QPushButton("⏸️ Pause")
        self.pause_button.setFixedSize(140, 40)
        self.pause_button.setStyleSheet(button_stylesheet)
        self.pause_button.clicked.connect(self.pause_scraping)
        second_buttons_layout.addWidget(self.pause_button)

        # Add a horizontal spacer to increase space between top buttons and browse button
        horizontal_spacer_top2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        second_buttons_layout.addItem(horizontal_spacer_top2)

        self.resume_button = QPushButton("⏯️ Resume")
        self.resume_button.setFixedSize(140, 40)
        self.resume_button.setStyleSheet(button_stylesheet)
        self.resume_button.clicked.connect(self.resume_scraping)
        second_buttons_layout.addWidget(self.resume_button)

        # Add a horizontal spacer to increase space between top buttons and browse button
        horizontal_spacer_top3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        second_buttons_layout.addItem(horizontal_spacer_top3)

        self.na_button = QPushButton("NA")
        self.na_button.setFixedSize(140, 40)
        self.na_button.setStyleSheet(button_stylesheet)
        second_buttons_layout.addWidget(self.na_button)

        # Add a spacer to push buttons to the left
        second_buttons_layout.addStretch(1)

        controls_layout.addLayout(second_buttons_layout)

        # Add a vertical spacer to increase space between progress bar and export buttons
        vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)
        controls_layout.addItem(vertical_spacer) 

        # File selection layout with Total domains label on top
        file_selection_layout = QVBoxLayout()

        self.domain_count_label = QLabel("Total domains: 0")
        file_selection_layout.addWidget(self.domain_count_label)

        file_layout = QHBoxLayout()

        self.browse_button = QPushButton()
        self.browse_button.setFixedSize(160, 60)
        self.browse_button.setIcon(QIcon('phoneScrapper/browser_icon.png'))
        self.browse_button.setIconSize(QSize(160, 55))
        self.browse_button.setStyleSheet("padding: 0px; border: 1px solid black;")
        self.browse_button.clicked.connect(self.browse_file)
        file_layout.addWidget(self.browse_button)

        horizontal_spacer_file_browser = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        file_layout.addItem(horizontal_spacer_file_browser)

        self.file_path_label = QLabel("")
        self.file_path_label.setFixedSize(300, 30)
        self.file_path_label.setMaximumWidth(400)
        self.file_path_label.setStyleSheet("border: 1px solid lightgray;")
        file_layout.addWidget(self.file_path_label)

        file_layout.addStretch(1)

        file_selection_layout.addLayout(file_layout)

        controls_layout.addLayout(file_selection_layout)

        # Add a vertical spacer to increase space between progress bar and export buttons
        vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)
        controls_layout.addItem(vertical_spacer) 

        # Labels for counts
        label_container = QFrame()
        label_container.setFrameShape(QFrame.StyledPanel)
        label_container.setStyleSheet("QFrame { border: 1px solid black; padding: 10px; }")

        # Create a layout for the container
        container_layout = QVBoxLayout(label_container)

        def create_label(text):
            label = QLabel(text)
            label.setStyleSheet("QLabel { border: none; }")  # Ensure no border or other styles are applied to the labels
            return label

        # Create the labels
        self.total_urls_processed_label = create_label("URLs Processed: 0")
        container_layout.addWidget(self.total_urls_processed_label)

        self.total_contact_found_label = create_label("Contact Numbers Found: 0")
        container_layout.addWidget(self.total_contact_found_label)

        self.total_contact_not_found_label = create_label("Contact Numbers Not Found: 0")
        container_layout.addWidget(self.total_contact_not_found_label)

        self.success_rate_label = create_label("Contact Success Rate: 0%")
        container_layout.addWidget(self.success_rate_label)

        # Add the container to the main layout
        controls_layout.addWidget(label_container)

        # Add a vertical spacer to increase space between progress bar and export buttons
        vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)
        controls_layout.addItem(vertical_spacer) 

        # Progress bar layout
        progress_layout = QVBoxLayout()

        self.progress_bar = QProgressBar()
        progress_layout.addWidget(self.progress_bar)

        self.time_layout = QHBoxLayout()
        progress_layout.addLayout(self.time_layout)

        self.time_label = QLabel("Elapsed time: 0s")
        self.time_layout.addWidget(self.time_label)

        # Add a fixed spacer to increase space between time labels
        time_fixed_spacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.time_layout.addItem(time_fixed_spacer)  # This spacer adds fixed space

        self.remaining_label = QLabel("Time remaining: Calculating...")
        self.time_layout.addWidget(self.remaining_label)

        # Add a horizontal spacer to ensure equal spacing from the right
        horizontal_spacer_controls_p = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        progress_layout.addItem(horizontal_spacer_controls_p)

        controls_layout.addLayout(progress_layout)

        # Single Data View layout
        single_data_layout = QHBoxLayout()

        self.single_url_input = QLineEdit()
        self.single_url_input.setPlaceholderText("SINGLE DATA VIEW")
        self.single_url_input.setFixedSize(390, 30)
        single_data_layout.addWidget(self.single_url_input)
        single_data_layout.setAlignment(Qt.AlignLeft)

        self.single_start_button = QPushButton()
        self.single_start_button.setFixedSize(50, 30)
        self.single_start_button.setStyleSheet(single_button_stylesheet)
        self.single_start_button.setIcon(QIcon('phoneScrapper/start_icon.png'))  # Path to your PNG file
        self.single_start_button.setIconSize(QSize(40, 20))
        self.single_start_button.clicked.connect(self.start_single_scraping)
        single_data_layout.addWidget(self.single_start_button)

        controls_layout.addLayout(single_data_layout)

        # Add a vertical spacer to increase space between top buttons and browse button
        vertical_spacer_top = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)
        controls_layout.addItem(vertical_spacer_top)

        # Save buttons layout
        save_layout = QHBoxLayout()

        self.save_csv_button = IconAfterTextButton("Export as CSV", 'phoneScrapper/csv.png', icon_size=QSize(80, 20))
        self.save_csv_button.setFixedSize(150, 40)
        self.save_csv_button.setStyleSheet(save_csv_button_stylesheet)
        self.save_csv_button.clicked.connect(lambda: self.save_results('csv'))
        save_layout.addWidget(self.save_csv_button)

        # Add a vertical line between the buttons with fixed height
        vertical_line = QFrame()
        vertical_line.setFrameShape(QFrame.VLine)
        vertical_line.setFrameShadow(QFrame.Sunken)
        vertical_line.setFixedHeight(self.save_csv_button.height())  # Set fixed height to match button height
        save_layout.addWidget(vertical_line)

        self.save_excel_button = IconAfterTextButton("Export as Excel", 'phoneScrapper/excel.png', icon_size=QSize(40, 20))
        self.save_excel_button.setFixedSize(150, 40)
        self.save_excel_button.setStyleSheet(save_excel_button_stylesheet)
        self.save_excel_button.clicked.connect(lambda: self.save_results('xlsx'))
        save_layout.addWidget(self.save_excel_button)

        # Add a stretch to push buttons to the right
        save_layout.addStretch()

        # Create a container widget for the save_layout to set alignment
        save_container = QWidget()
        save_container.setLayout(save_layout)
        save_container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # Align the save_container to the right
        controls_layout.addWidget(save_container, alignment=Qt.AlignRight)


        # Add a spacer to push everything to the left
        controls_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Reduce space at the bottom
        controls_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed))

        # Add logo and copyright text
        logo_widget = QWidget()
        logo_layout = QHBoxLayout(logo_widget)

        self.logo_label = QLabel()
        self.logo_label.setPixmap(QPixmap('phoneScrapper/Concentrix.png').scaled(30, 30, Qt.KeepAspectRatio))
        self.logo_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        logo_layout.addWidget(self.logo_label)

        self.copyright_label = QLabel("@ Copyright Product by CR Consultancy Service PVT LTD.")
        self.copyright_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.copyright_label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        logo_layout.addWidget(self.copyright_label)

        logo_layout.setContentsMargins(0, 0, 0, 0)
        logo_layout.setSpacing(5)  # Adjust this value for slight gap

        logo_widget.setStyleSheet("background-color: #eff1fd;")

        controls_layout.addWidget(logo_widget)
        
        # Create a wrapper widget to contain the control layout with the gradient
        controls_wrapper = QWidget()
        controls_wrapper.setLayout(controls_layout)

        # Add the table layout and controls wrapper to the main layout
        main_layout.addLayout(table_layout)
        main_layout.addWidget(controls_wrapper)

        # Set the stretch factors
        main_layout.setStretch(0, 8)
        main_layout.setStretch(1, 2) 
        main_layout.addStretch()

        self.setCentralWidget(main_widget)

        # Timer to update elapsed time and remaining time
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)