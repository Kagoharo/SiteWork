import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="postgres",
                                  password="123",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="site")

    cursor = connection.cursor()

    product_categories = [
        ("Software", "Contains various software products for your PC"),
        ("Electronics", "Category that contains electronic goods such as mobile phones, PC, TV etc."),
        ("Appliances", "Contains goods such as dishwasher, washer, microwave etc."),
        ("Books", "Contains books in audio format, electronic books, physical copies of books"),
        ("HouseAccessories","Contains different accessories for your house"),
    ]

    product_categories_records = ", ".join(["%s"] * len(product_categories))

    insert_query = (
        f"INSERT INTO product_categories (category, description) VALUES {product_categories_records}"
    )

    connection.autocommit = True
    cursor.execute(insert_query, product_categories)

    products = [
        ("Adobe Photoshop for Windows 11", "MultiFunctional graphical editor. Usually works with bitmaps but also has some tools for vector graphics", 20000, 1000, 1),
        ("Windows 11 Professional", "Operational system for PC that is developed by Microsoft. It's the latest version of Windows by now.", 30000, 1000, 1),
        ("Adobe Premiere Pro", "Professional version of Adobe Premiere that includes some advanced features to work with.", 25000, 1000,  1),
        ("FL Studio", "Digital sound workstation and sequencer for writing music", 10000, 1000, 1),
        ("Microsoft Office 2019", "Set of programs for solving various office tasks", 15000, 1000, 1),
        ("AnyLogic", "Software for simulation modeling. ", 10000, 1000, 1),
        ("MathLab", "Software package for solving technical computing problems", 21000, 1000, 1),
        ("AutoCAD", "2D and 3D CAD / CAM system developed by Autodesk.", 30000, 1000, 1),
        ("Autodesk 3Ds Max", "Professional 3D modeling, animation and rendering software for game creation and design.", 30000, 1000, 1),
        ("Kaspersky Internet Security", "Line of software products developed by Kaspersky Lab on the basis of Kaspersky Anti-Virus for comprehensive protection of home personal computers and mobile devices in real time from known and new threats.", 30000, 500, 1),
        ("WinRar", "File archiver for 32- and 64-bit Windows operating systems, which allows you to create, modify and unpack RAR and ZIP archives, as well as work with many other archives formats.y", 15000, 1000, 1),
        ("iPhone 11 PRO Max 512GB", "In fact, an enlarged copy of the iPhone 11 Pro, with the characteristic 'Max' prefix in the name. It differs mainly in larger and larger dimensions.", 80000, 1000, 2),
        ("Samsung / Телевизор UE24N4500AUXRU", "Compact TV Samsung UE24N4500AU is made in a modern laconic design, making it easy to fit into the surrounding space. The 24-inch diagonal is ideal for comfortable viewing of TV programs or movies in the kitchen, bedroom or anywhere else. Place the device on a horizontal surface or hang it on a wall using an arm that supports VESA mount.", 15000, 100, 2),
        ("NoteBook Extensa 15 EX215-53G-38AQ", "The 15.6-inch narrow bezel display creates a taller screen-to-body ratio. In addition, ComfyView technology reduces glare by limiting reflected light for a more comfortable on-screen viewing experience. Working from home is more convenient than ever. The cleverly positioned Wi-Fi 5 (802.11ac) antenna with MU-MIMO technology ensures a reliable wireless signal. An optimized digital webcam, microphone and two built-in stereo speakers deliver superior sound and picture quality.", 44367, 300, 2),
        ("Console PS5", "Game console with high performance, beautiful design, and acceptable cost.", 49990, 100, 2),
        ("Console Xbox Series X", "Game console with highest performance beneath others with minimalistic strict design and hundreds of games available.", 60000, 100, 2),
        ("Vacuum cleaner Philips PowerPro Expert", "The Philips PowerPro Expert canister vacuum cleaner delivers great results on all floors. PowerCyclone 8 technology rapidly accelerates air flow in the cyclone chamber to separate dust particles. The TriActive + nozzle lifts the carpet pile for a thorough cleaning. Air ducts in the front pick up coarse debris, while the brushes on the sides clean the floor along the walls and furniture.", 14000, 50, 3),
        ("Iron Philips GC4535/20", "Thanks to the innovative design, scale particles are easily broken down and automatically collected in a special removable container. This allows you to descale your appliance in less than 15 seconds for superior appliance results. Powerful and constant flow allows more steam to enter the fabric and smoothes creases faster. Steam penetrates deep into the fabric to easily remove stubborn creases.", 4000, 100, 3),
        ("Polaris PVCR0926W", "Dry and wet cleaning. Battery life: up to 200 minutes. Cleaning according to the schedule. HEPA 12 filter. Power button on the body. Automatic return to base. Infrared sensors for indoor orientation. Glass top panel. Electric brush. Side brushes for efficient cleaning. Flat design for easy cleaning under furniture. The volume of the dust container is 0.5 liters. The volume of the container for wet cleaning is 0.3 l (water) + 0.2 l (dust). Maximum power of the device: 25 W.", 1500, 230, 3),
        ("Multicooker PMC 0526 IQ Home", "Wi-Fi multicooker. 300 cooking modes. 700+ recipes in the IQ Home app from the chefs of the Gastronom magazine. 21 automatic cooking programs. Function: My Prescription PLUS. Operating modes: My recipe plus, Baking, Soup, Stewing, Frying, Baking, Jellied meat, Yogurt, Jam, Steaming, Milk porridge, Groats, Heating, Pilaf, Omelet, Simmering, Tincture, Bread, Frying in oil, Su- kind, Oatmeal. Program saving in case of power failure 2 hours.", 6499, 100, 3),
        ("Electric kettle PWK 1753CGL", "Convenient water filling without opening the lid. Innovative steel at the bottom of the kettle. Extremely easy cleaning. High quality heat-resistant glass body. Instrumental check of glass homogeneity and purity. Double-sided scale for water level control. Filter for water purification. Automatic and manual switch. Concealed heating element. Connection via stand. Blocking of inclusion without water. Overheat protection. Capacity: 1.5 l. Power: 1800-1950 W.", 2499, 50, 3),
        ("Refrigerator ATLANTХМ-6023-031", "Refrigerators ATLANT SOFT LINE series are an excellent choice for those who want to create a cozy and soft atmosphere in the kitchen. Pleasant rounded shapes, slightly convex doors, comfortable handles - and an overall feeling of tranquility and comfort. Integrated end handles in the 'Soft Line' style complement the pleasant shape of the refrigerator, have a comfortable grip for the hand when opening the door and reduce overall dimensions in depth.", 500, 80, 3),
        ("Book Mysterious Island", "The Mysterious Island is a book worth taking with you to a desert island. One of Jules Verne's most entertaining novels, a gripping story of the adventures of the islanders, a survival guide and a hymn to human willpower and courage. The adventurous plot of the novel includes a storm, a volcanic eruption, an attack by pirates, the mysterious Captain Nemo and a story about survival on a piece of land. After reading this book, you can learn how to make soap.", 500, 50, 4),
        ("Book Count of Monte Cristo ", "The Count of Monte Cristo, one of the most popular novels by Alexandre Dumas, is an overwhelming success with readers. The author took its plot from the archives of the Parisian police. The real life of the shoemaker François Picot, who became the prototype of Edmond Dantes, under the pen of a real artist turned into a gripping book about the martyr of the Château d'If and the Parisian angel of vengeance. ", 500, 40, 4),
        ("Book 1984", "1984 is a warning novel about the danger of totalitarianism, one of the most famous dystopias of the XX century, standing on a par with Zamyatin's We, Huxley's Brave New World and Bradbury's Fahrenheit 451. The novel made it to the BBC's 200 Best Books and The Times 60 Best Books of the Past 60 Year.",450, 40, 4),
        ("Bathroom hook ", "Set of hooks for the bathroom 6 pcs. Complete set MIX. Wall Hooks are a simple and versatile tool that makes it easy to store bathrobes, towels, accessories and other small items in the bathroom and kitchen. Installation of such a holder takes literally a few seconds and does not require drilling into the wall. ", 1000, 20, 5),
        ("lunch-box", "Silicone lunch box. The collapsible container made of silicone is a convenient and lightweight container for storing and transporting sandwiches, portioned salads, meat or fish, hot and cold dishes, even liquid products. The container is completely sealed. The plastic cover is equipped with four special latches and a silicone seal. ", 199, 20, 5),
    ]

    products_records = ", ".join(["%s"] * len(products))

    insert_query = (
        f"INSERT INTO product (name, description, price, amount, pcID) VALUES {products_records}"
    )

    connection.autocommit = True
    cursor.execute(insert_query, products)

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")