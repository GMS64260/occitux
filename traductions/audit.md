# Audit des catalogues occitans d'Ubuntu 24.04

Les catalogues décompilés par `msgunfmt` sont identifiés dans [provenance.json](provenance.json).
L'audit lexical parcourt toutes leurs entrées. Il distingue les différences intégrées
des chaînes conservées en attente de validation complète. Il ne certifie pas les chaînes
sans différence repérée. [audit.csv](audit.csv) fournit les clés et contextes exacts.

| Domaine | Entrées oc sources | Delta béarnais | Différences différées |
|---|---:|---:|---:|
| xfce4-panel | 489 | 195 | 38 |
| xfce4-session | 161 | 72 | 22 |
| xfdesktop | 257 | 105 | 28 |
| thunar | 833 | 298 | 100 |
| xfwm4 | 179 | 60 | 31 |
| tuxpaint | 123 | 31 | 2 |
| lightdm | 0 | 0 | 0 |
| ristretto | 179 | 69 | 5 |
| xfce4-pulseaudio-plugin | 26 | 7 | 2 |
| lightdm-gtk-greeter | 25 | 18 | 1 |

Le domaine `lightdm` est vide dans le paquet ; les libellés de connexion se trouvent
dans `lightdm-gtk-greeter`, ajouté à l'audit. Aucune chaîne n'est inventée dans le domaine vide.

Les deltas ne remplacent pas directement les MO installés : voir le repli dans [README.md](README.md).

## xfce4-panel

| Clé source | Occitan livré | Béarnais retenu ou motif de conservation | Glossaire |
|---|---|---|---|
| %1 o'clock | %1 ora | %1 òra | heure |
| 24-_hour clock | Relòtge 24 _oras | Relòtge 24 _òras | heure |
| <b>Compositing is currently disabled</b><br>Enable compositing in the window manager for opacity settings in the panel. | <b>La composision es actualament desactivada</b><br>Activar la composision dins lo gestionari de fenèstra per afichar los paramètres d’opacitat dins lo panèl. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | dans \| fenetre \| panneau |
| <b>General</b> | <b>General</b> | <b>Generau</b> | general |
| Add Appli_cation | A_pondre una aplicacion | _Ajustar ua aplicacion | ajouter \| une |
| Add New Item | Apondre un element | Ajustar un element | ajouter |
| Add New Items | Apondre d'elements novèls | Ajustar d'elements navèths | ajouter \| nouveau |
| Add Workspace | Apondre un espaci de trabalh | Ajustar un espaci de tribalh | ajouter \| travail |
| Add _New Items... | Apondre d'elements _novèls ... | Ajustar d'elements _navèths ... | ajouter \| nouveau |
| Add a new empty item | Apondre un novèl element void | Ajustar un navèth element vueit | ajouter \| nouveau \| vide |
| Add a new hyperlink | Apondre un novèl iperligam | Ajustar un navèth iperligam | ajouter \| nouveau |
| Add a new launcher to the panel based on the information of this desktop file | Apondre un aviador novèl dins lo tablèu de bòrd amb las informacions d'aqueste fichièr del burèu | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | ajouter \| avec \| dans \| du \| fichier \| nouveau \| panneau |
| Add a new panel | Apondre un novèl tablèu de bòrd | Ajustar un navèth panèu | ajouter \| nouveau \| panneau |
| Add a new plugin to the panel | Apondre un empeuton novèl al tablèu de bòrd | Ajustar un empeuton navèth au panèu | ajouter \| au \| nouveau \| panneau |
| Add new item to this panel | Apondre un element novèl al tablèu de bòrd | Ajustar un element navèth au panèu | ajouter \| au \| nouveau \| panneau |
| Add one or more existing items to the launcher | Apondre un o mantun element qu'existisson dins l'aviador | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | ajouter \| dans |
| Afternoon | Aprèp miègjorn | Aprèp mieidia | midi |
| Almost noon | Gaireben miègjorn | Gaireben mieidia | midi |
| Are you sure you want to clear the list of known items? | Volètz vertadièrament suprimir la lista dels elements coneguts ? | Suprimir la lista deus elements coneguts ? | supprimer \| liste \| des \| element |
| Are you sure you want to log out? | Sètz segur que vos volètz desconnectar ? | Barrar la session ? | fermer_session |
| Are you sure you want to quit the panel? | Sètz segur que volètz quitar lo tablèu de bòrd ? | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | panneau |
| Are you sure you want to remove panel %d? | Sètz segur que volètz suprimir lo tablèu de bòrd %d ? | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | panneau |
| Are you sure you want to restart? | Sètz segur que volètz reamodar ? | Tornar aviar ? | redemarrer |
| Are you sure you want to shut down? | Sètz segur que volètz atudar ? | Estupar ? | eteindre |
| Arrange _items in a single row | Arrengar los _elements en una sola colomna | Arrengar los _elements en ua sola linha | element \| une \| ligne |
| Au_tomatically hide the panel: | Amagar lo panèl au_tomaticament : | Amagar lo panèu au_tomaticament : | panneau |
| Because the panel is running in kiosk mode, you are not allowed to make changes to the panel configuration as a regular user | Perque lo tablèu de bòrd es en cors d'execucion en mòde restrench, sètz pas autorizat a aportar de modificacions a la configuracion del tablèu de bòrd en tant qu'utilizaire regular | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | du \| panneau \| utilisateur |
| Binary time | Ora binària | Òra binària | heure |
| Button _title: | _Títol del boton : | _Títol deu boton : | du |
| C_lear Known Items | E_scafar los elements coneguts | De_sfaçar los elements coneguts | effacer |
| Calendar | Calendièr | Calendari | calendrier |
| Clear | Escafar | Desfaçar | effacer |
| Clock Options | Opcions del relòtge | Opcions deu relòtge | du |
| Close Window | Tampar la fenèstra | Barrar la frinèsta | fenetre \| fermer |
| Create & _Open | Crear e _dobrir | Crear & _obrir | creer \| ouvrir |
| Create Folder... | Crear un dorsièr… | Crear un dossièr… | dossier |
| Create Launcher on the panel | Crear un aviador sul tablèu de bòrd | Crear un aviador suu panèu | panneau \| sur_le |
| Create New Folder | Crear un dorsièr novèl | Crear un dossièr navèth | dossier \| nouveau |
| Create New Text Document | Crear document de tèxt novèl | Crear document de tèxte navèth | nouveau \| texte |
| Create new launcher from %d desktop file | Crear un aviador a partir de %d fichièr de burèu / Crear un aviador a partir de %d fichièrs de burèu | Conservé : Pluriel gettext : validation de toutes les formes requise. |  |
| Customize the panel | Personalizar lo tablèu de bòrd | Personalizar lo panèu | panneau |
| D_raw window frame when hovering a button | A_fichar lo quadre de la fenèstra al susvòl d'un boton | A_fichar lo quadre de la frinèsta au susvòl d'un boton | au \| fenetre |
| Date, then time | Data, puèi ora | Data, puish òra | ensuite \| heure |
| Directory Menu | Menú de repertòri | Menú de dossièr | dossier |
| Do you want to start the panel? If you do, make sure you save the session on logout, so the panel is automatically started the next time you login. | Volètz aviar lo tablèu de bòrd ? Se òc, atencion que la sesilha siá salvada al moment de la desconnexion, de tal biais que lo tablèu de bòrd siá reaviat a la dobèrtura de sesilha que ven. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | au \| panneau \| session |
| Do you want to suspend to RAM? | Volètz metre en velha en memòria viva ? | Méter en velha en memòria viva ? | mettre |
| Do you want to suspend to disk? | Volètz metre en velha sul disc ? | Méter en velha suu disc ? | mettre \| sur_le \| disque |
| Early morning | D'ora lo matin | D'òra lo matin | heure |
| Ed_it Menu | E_ditar lo menú | Mo_dificar lo menú | modifier |
| Edit the currently selected item | Editar l'element actualament seleccionat | Modificar l'element actualament seleccionat | modifier |
| Enter a list of patterns that will be used to determine which files are visible in a directory. If you specify more than one pattern here, the list items must be separated with semicolons (e.g. *.txt;*.doc). | Entratz una lista de modèls que seràn utilizats per determinar quines fichièrs son visibles dins un repertòri. Se especificatz mai d'un modèl aicí, los elements de la lista devon èsser separats per de punts-virgulas (per exemple *.txt;*. doc). | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | dans \| dossier \| fichier \| ici \| modele \| plus \| une |
| Enter search phrase here | Picatz vòstres tèrmes de recèrca aicí | Picar los mots de recèrca ací | saisir \| mot \| recherche \| ici |
| Enter the new name: | Entrar lo novèl nom : | Entrar lo navèth nom : | nouveau |
| Failed to acquire manager selection for screen %d | Impossible d'aquerir la seleccion del gestionari per l'ecran %d | Impossible d'aquerir la seleccion deu gestionari per l'ecran %d | du |
| Failed to add a plugin to the panel | Impossible d'apondre un empeuton dins lo tablèu de bòrd | Impossible d'ajustar un empeuton dens lo panèu | ajouter \| dans \| panneau |
| Failed to create folder: %s | Creacion impossibla del dorsièr : %s | Creacion impossibla deu dossièr : %s | dossier \| du |
| Failed to execute clock command | Impossible d'executar la comanda del relòtge | Impossible d'executar la comanda deu relòtge | du |
| Failed to open desktop item editor | Impossible de dobrir l'editor d'elements de burèu | Impossible d'obrir l'editor d'elements de burèu | ouvrir |
| Failed to query content type for "%s" | Impossible de questionar lo tipe de contengut per « %s » | Impossible de questionar lo tipe de contiengut per « %s » | contenu |
| Failed to quit the panel | Impossible de quitar lo tablèu de bòrd | Impossible de quitar lo panèu | panneau |
| Failed to restart the panel | Impossible de reaviar lo tablèu de bòrd | Impossible de tornar aviar lo panèu | panneau \| redemarrer |
| Failed to save the panel configuration | Impossible d'enregistrar la configuracion del tablèu de bòrd | Impossible d'enregistrar la configuracion deu panèu | du \| panneau |
| Failed to send D-Bus message | Impossible de mandar un messatge D-Bus | Impossible d'enviar un messatge D-Bus | envoyer |
| Failed to show the add new items dialog | Impossible d'afichar la bóstia de dialòg « Apondre d'elements novèls » | Impossible d'afichar la bóstia de dialòg « Ajustar d'elements navèths » | ajouter \| nouveau |
| General | General | Generau | general |
| Group title and timestamp | Títol del grop e orodatatge | Títol deu grop e orodatatge | du |
| Group title and window title | Títol del grop e de la fenèstra | Títol deu grop e de la frinèsta | du \| fenetre |
| Hibernating and Suspending computer in %d seconds. | Ibernacion e interrupcion de l’ordenador d’aquí %d segondas. | Ibernacion e interrupcion de l’ordinator d’aquí %d segondas. | ordinateur |
| Hibernating computer in %d seconds. | Mesa en velha perlongada dins %d segondas. | Mesa en velha perlongada dens %d segondas. | dans |
| If enabled, ensure that the items are laid out in a single row | Se activat, s’assegura que los elements son agençats sus una sola colomna | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | une |
| If set, this command is run when the plugin is left-clicked, instead of displaying the default calendar. | Se definit, aquesta comanda es executada quand l’empeuton es clicat amb clic esquèr, a la plaça d’afichar lo calendièr per defaut. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | avec \| calendrier |
| If you remove the item from the panel, it is permanently lost. | Se suprimissètz l'element del tablèu de bòrd, o serà definitivament. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | du \| panneau |
| Item buttons will take a square when it's possible | Los botons dels elements seràn carrats quand es possible | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | des |
| Launch New Instance | Aviar instància novèla | Aviar instància navèra | nouvelle |
| Log Out | Desconnexion | Barrar la session | fermer_session |
| Log Out... | Desconnexion… | Barrar la session… | fermer_session |
| Log _Out | Des_connexion | Barrar la _session | fermer_session |
| Log _Out... | _Desconnexion… | Barrar la _session… | fermer_session |
| Log out, lock or other system actions | Desconnexion, varrolhatge o autras accions sistèma | Desconnexion, varrolhatge o autas accions sistèma | autre |
| Logging out in %d seconds. | Desconnexion dins %d segondas. | Barrar la session dens %d segondas. | fermer_session \| dans \| seconde |
| Menu File | Fichièr de menú | Fichèr de menú | fichier |
| Menu _file: | _Fichièr menú : | _Fichèr menú : | fichier |
| Mi_ddle click action: | Accion del clic del mitan : | Accion deu clic deu _miei : | du \| milieu |
| Minimize Window | Minimizar la fenèstra | Minimizar la frinèsta | fenetre |
| Modifying the panel is not allowed | Modificacion del tablèu de bòrd interdicha | Modificacion deu panèu interdicha | du \| panneau |
| Most likely another widget took over the function of a notification area. This area will be unused. | Es probable qu'una autra aplicacion aja pres la foncion de zòna de notificacion. Aquesta zòna demorarà inutilizada. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | autre \| une |
| Move currently selected item down by one row | Desplaçar l'element actualament seleccionat d'una linha cap aval | Desplaçar l'element actualament seleccionat d'ua linha cap aval | une |
| Move currently selected item up by one row | Desplaçar l'element actualament seleccionat d'una linha cap amont | Desplaçar l'element actualament seleccionat d'ua linha cap amont | une |
| Move the selected item one row down | Desplaçar l'element seleccionat d'una linha cap aval | Desplaçar l'element seleccionat d'ua linha cap aval | une |
| Move the selected item one row up | Desplaçar l'element seleccionat d'una linha cap amont | Desplaçar l'element seleccionat d'ua linha cap amont | une |
| Name %s lost on the message dbus, exiting. | Nom %s perdut sul messatge dbus, sortida. | Nom %s perdut suu messatge dbus, sortida. | sur_le |
| Name of a timezone corresponding a file in the zoneinfo database, for example "America/New_York". Leave empty to use the localtime. | Lo nom d'un fus orari que correspond a un fichièr dins la banca de donadas zoneinfo, per exemple « America / Nòva York ». Daissatz void per utilizar l'ora locala. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | dans \| donnees \| fichier \| heure \| nouvelle \| vide |
| Never | Pas jamai | Pas jamèi | jamais |
| New Instance | Instància novèla | Instància navèra | nouvelle |
| New _Application | No_vèla aplicacion | Na_vèra aplicacion | nouvelle |
| New _Link | Ligam n_ovèl | Ligam _navèth | nouveau |
| Night | Nuèch | Nueit | nuit |
| No Windows | Pas cap de fenèstra | Pas cap de frinèsta | fenetre |
| Noon | Miègjorn | Mieidia | midi |
| Open Folder | Dobrir lo repertòri | Obrir lo dossièr | dossier \| ouvrir |
| Open in Terminal | Dobrir dins un terminal | Obrir dens un terminal | dans \| ouvrir |
| Open launcher menu | Dobrir lo menú de l'aviador | Obrir lo menú de l'aviador | ouvrir |
| Pane_l | Tablèu de _bòrd | _Panèu | panneau |
| Panel | Tablèu de bòrd | Panèu | panneau |
| Panel %d | Tablèu de bòrd %d | Panèu %d | panneau |
| Panel Pr_eferences... | Pr_eferéncias del tablèu de bòrd... | Pr_eferéncias deu panèu... | du \| panneau |
| Panel Preferences | Preferéncias del panèl | Preferéncias deu panèu | du \| panneau |
| Panel config needs migration... | La configuracion del tablèu de bòrd deu èsser migrada... | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | du \| panneau |
| Panel configuration has been updated. | La configuracion del tablèu de bòrd es estada mesa a jorn. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | du \| jour \| panneau |
| Pick a Panel Color | Seleccionar una color del tablèu de bòrd | Seleccionar ua color deu panèu | du \| panneau \| une |
| Please choose a panel for the new plugin: | Seleccionatz un tablèu de bòrd per l'empeuton novèl : | Seleccionar un panèu entà l'empeuton navèth : | selectionner \| pour \| nouveau \| panneau |
| Plugin "%s" unexpectedly left the panel, do you want to restart it? | L'empeuton « %s » a quitat lo tablèu de bòrd d'un biais imprevist. Lo volètz reaviar ? | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | panneau \| redemarrer |
| Popup menu at current mouse position | Menú contextual a la posicion actuala de la mirga | Menú contextual a la posicion actuau de la soritz | actuel \| souris |
| Program launcher with optional menu | Aviador de programa amb menú facultatiu | Aviador de programa dab menú facultatiu | avec |
| Provides status notifier items (application indicators) and legacy systray items | Provesís d’elements de notificacion d’estat (indicador d’aplicacion) e d’elements de barra d’estat coma sempre | Provesís d’elements de notificacion d’estat (indicador d’aplicacion) e d’elements de barra d’estat com sempre | comme |
| Quit the running panel instance | Quitar l'instància del tablèu de bòrd en cors d'execucion | Quitar l'instància deu panèu en cors d'execucion | du \| panneau |
| Remove Workspace "%s" | Suprimir l'espaci de trabalh « %s » | Suprimir l'espaci de tribalh « %s » | travail |
| Remove Workspace %d | Suprimir l'espaci de trabalh %d | Suprimir l'espaci de tribalh %d | travail |
| Remove the currently selected panel | Suprimir lo tablèu de bòrd actualament seleccionat | Suprimir lo panèu actualament seleccionat | panneau |
| Removing the item from the panel also means its configuration will be lost. | Suprimir l’element del panèl significa tanben que sa configuracion serà perduda. | Suprimir l’element deu panèu significa tanben que sa configuracion serà perduda. | du \| panneau |
| Resets the list of items and their visibility settings | Reïnicializar la lista dels elements e lor paramètres de visibilitat | Tornar inicializar la lista deus elements e lor paramètres de visibilitat | des \| reinitialiser |
| Restart | Reamodar | Tornar aviar | redemarrer |
| Restart the running panel instance | Reamodar l'instància del tablèu de bòrd en cors d'execucion | Tornar aviar l'instància deu panèu en cors d'execucion | du \| panneau \| redemarrer |
| Restarting computer in %d seconds. | Reamodament de l'ordenador dins %d segondas. | Tornar aviar l'ordinator dens %d segondas. | redemarrer \| ordinateur \| dans \| seconde |
| Restarting... | Reaviada... | Tornar aviar... | redemarrer |
| Restore minimized windows to current _workspace | Restablir las fenèstras redusidas dins l'_espaci de trabalh corrent | Conservé : Flexion nouvelle non attestée dans les sources consultées. | dans \| travail |
| Save the panel configuration | Enregistrar la configuracion del tablèu de bòrd | Enregistrar la configuracion deu panèu | du \| panneau |
| Select A Directory | Seleccionar un repertòri | Seleccionar un dossièr | dossier |
| Select A Menu File | Seleccionar un fichièr de menú | Seleccionar un fichèr de menú | fichier |
| Select this option if you don't want maximized windows to cover the area behind the panel. This only works when the panel is attached to a screen edge. | Causissètz aquesta opcion se volètz pas que las fenèstra maximalizadas cobriscan la zòna darrièr lo panèl. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | derriere \| fenetre \| panneau |
| Select this option to automatically increase the length of the panel if the plugins request more space. | Seleccionatz aquesta opcion per aumentar automaticament la longor del tablèu de bòrd se los empeutons demandan mai d'espaci. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | du \| panneau \| plus |
| Select this option to disable the tooltips when moving over the panel button or menu items. | Seleccionatz aquesta opcion per desactivar las infobullas quand la mirga se desplaça sul boton del tablèu de bòrd o los elements del menú. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | du \| panneau \| souris \| sur_le |
| Select this option to extend the panel over multiple monitors. | Seleccionatz aquesta opcion per espandir lo tablèu de bòrd sus mantun monitor. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | panneau |
| Select this option to hide the handles of the panel and lock its position. | Seleccionatz aquesta opcion per amagar las ponhadas del tablèu de bòrd e varrolhar sa posicion. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | du \| panneau |
| Select this option to move the clicked menu item to the panel. | Seleccionatz aquesta opcion per desplaçar l'element del menú clicat sul tablèu de bòrd. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | du \| panneau \| sur_le |
| Select this option to show the generic application name in the menu, for example "File Manager" instead of "Thunar" | Seleccionatz aquesta opcion per afichar lo nom generic de l'aplicacion dins lo menú, per exemple « Gestionari de fichièrs » al luòc de « Thunar » | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | au \| dans \| fichier |
| Session Menu | Menú sesilha | Menú session | session |
| Show 'New Text _Document' | Afichar « _Document de tèxt novèl » | Afichar « _Document de tèxte navèth » | nouveau \| texte |
| Show 'Open in _Terminal' | Afichar « Dobrir dins un terminal » | Afichar « Obrir dens un _terminal » | afficher \| ouvrir \| dans |
| Show '_New Folder' | Afichar « Dorsièr _novèl » | Afichar « Dossièr _navèth » | dossier \| nouveau |
| Show '_Open _Folder' | Afichar « Dobrir lo dorsièr » | Afichar « _Obrir lo _dossièr » | afficher \| ouvrir \| dossier |
| Show _hidden files | Afichar los fichièrs ama_gats | Afichar los fichèrs ama_gats | fichier |
| Show a confirmation dialog with a 30 second timeout for some of the actions. | Afichar una bóstia de dialòg de confirmacion pendent 30 segondas per d'unas accions. | Afichar ua bóstia de dialòg de confirmacion pendent 30 segondas per d'unas accions. | une |
| Show a directory tree in a menu | Afichar una arborescéncia de repertòris dins un menú | Afichar ua arborescéncia de dossièrs dens un menú | dans \| dossier \| une |
| Show application d_escription in tooltip | Afichar la d_escripcion de l'aplicacion dins una infobulla | Afichar la d_escripcion de l'aplicacion dens ua infobulla | dans \| une |
| Show button _labels | Afichar los _noms dels botons | Afichar los _noms deus botons | des |
| Show gri_d | Afichar una _grasilha | Afichar ua _grasilha | une |
| Show ic_ons in menu | Afichar las _icònas dins lo menú | Afichar las _icònas dens lo menú | dans |
| Show last _used item in panel | Afichar lo _darrièr element utilizat dins lo tablèu de bòrd | Afichar lo _darrèr element utilizat dens lo panèu | dans \| derriere \| panneau |
| Show the 'Add New Items' dialog | Afichar la bóstia de dialòg 'Apondre d'elements novèls' | Afichar la bóstia de dialòg 'Ajustar d'elements navèths' | ajouter \| nouveau |
| Show the 'Panel Preferences' dialog | Afichar la bóstia de dialòg 'Preferéncias del tablèu de bòrd' | Afichar la bóstia de dialòg 'Preferéncias deu panèu' | du \| panneau |
| Show windows from _all workspaces | Afichar las _fenèstras de totes los espacis de trabalh | Conservé : Flexion nouvelle non attestée dans les sources consultées. | tous \| travail |
| Show windows from all mo_nitors | Afichar las fenèstras de totes los _monitors | Conservé : Flexion nouvelle non attestée dans les sources consultées. | tous |
| Show workspace _names | Afichar lo _nom dels espacis de trabalh | Afichar lo _nom deus espacis de tribalh | des \| travail |
| Show workspace a_ctions | Afichar las a_ccions dels espacis de trabalh | Afichar las a_ccions deus espacis de tribalh | des \| travail |
| Show workspace number | Afichar lo numèro de l'espaci de trabalh | Afichar lo numèro de l'espaci de tribalh | travail |
| Shut Down | Atudar | Estupar | eteindre |
| Shut _Down | A_tudar | Es_tupar | eteindre |
| Sorting _order: | Òr_dre de triada : | Òr_di de triada : | ordre |
| Span mo_nitors | Espandir a totes los moni_tors | Espandir a tots los moni_tors | tous |
| Suspending computer in %d seconds. | Mesa en velha de l'ordenador dins %d segondas. | Mesa en velha de l'ordinator dens %d segondas. | dans \| ordinateur |
| Switch User | Cambiar d'utilizaire | Cambiar d'utilizator | utilisateur |
| Switch between panel presets | Bascular entre los tablèus de bòrd predefinits | Bascular entre los panèus predefinits | panneau |
| Switch between virtual desktops | Cambiar de pòstes de trabalh virtuals | Cambiar de pòstes de tribalh virtuals | travail |
| Switch workspaces using the mouse wheel | Cambiar d'espaci de trabalh amb l'ajuda de la rodeta de la mirga | Cambiar d'espaci de tribalh dab l'ajuda de la rodeta de la soritz | avec \| souris \| travail |
| The Xfce development team. All rights reserved. | L'equipa de desvolopament de Xfce. Totes los dreches reservats. | L'equipa de desvolopament de Xfce. Tots los dreches reservats. | tous |
| The format describes the date and time parts to insert into the panel. For example, %Y will be substituted with the year, %m with the month and %d with the day. Similarly, &lt;b&gt;&lt;/b&gt; tags will make the text bold. See the &quot;Help&quot; page for additional information. | Lo format descriu las datas e oras de las pèças d'inserir dins lo panèl. Per exemple, %Y serà substituit a l'annada, %m pel mes e %d pel jorn. Amai, las balisas <b> </b> metràn lo tèxte en gras. Veire la pagina &quot; Ajuda &quot;  per mai d'informacions. | Conservé : Contexte technique ou long : relecture intégrale nécessaire. | dans \| heure \| jour \| panneau \| par_le \| plus \| voir |
| The format describes the date and time parts to insert into the panel. For example, %Y will be substituted with the year, %m with the month and %d with the day. Similarly, <b></b> tags will make the text bold. See the "Help" page for additional information. | Lo format descriu las datas e oras de las pèças d'inserir dins lo panèl. Per exemple, %Y serà substituit a l'annada, %m pel mes e %d pel jorn. Amai, las balisas <b> </b> metràn lo tèxte en gras. Veire la pagina «Ajuda» per mai d'informacions. | Conservé : Contexte technique ou long : relecture intégrale nécessaire. | dans \| heure \| jour \| panneau \| par_le \| plus \| voir |
| The panel and plugin configurations will be permanently removed | Las configuracions del tablèu de bòrd e dels empeutons seràn suprimidas definitivament | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | des \| du \| panneau |
| The panel of the Xfce Desktop Environment | Tablèu de bòrd de l'environament de burèu Xfce | Panèu de l'environament de burèu Xfce | panneau |
| The plugin restarted more than once in the last %d seconds. If you press Execute the panel will try to restart the plugin otherwise it will be permanently removed from the panel. | L'empeuton a reaviat mantun còp al cors de las %d darrièras segondas. Se quichatz sus Executar lo tablèu de bòrd va ensajar de reaviar l'empeuton siquenon serà suprimit definitivament del tablèu de bòrd. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | au \| derniere \| du \| panneau \| redemarrer |
| There is already a running instance | I a ja un tablèu de bòrd en cors d'execucion | I a dejà un panèu en cors d'execucion | deja \| panneau |
| This will create a new launcher plugin on the panel and inserts the dropped files as menu items. | Aquò va crear un empeuton d'aviada novèl sul tablèu de bòrd e inserirà los fichièrs depausats coma elements del menú. | Aquò va crear un empeuton d'aviada navèth suu panèu e inserirà los fichèrs depausats com elements deu menú. | comme \| du \| fichier \| nouveau \| panneau \| sur_le |
| Time | Ora | Òra | heure |
| Time Only | Ora solament | Òra solament | heure |
| Time Settings | Paramètres ora | Paramètres òra | heure |
| Time and Date _Settings... | Paramètres ora e data... | _Paramètres òra e data... | parametres \| heure \| date |
| Time, then date | Ora, puèi data | Òra, puish data | ensuite \| heure |
| Transparency when the pointer is not hovering over the panel, with 0 being fully transparent and 100 fully opaque. | Transparéncia quand la mirga susvòla pas lo tablèu de bòrd, 0 es transparent e 100 opac. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | panneau \| souris |
| Turning off computer in %d seconds. | Atudament dins %d segondas. | Estupar l'ordinator dens %d segondas. | eteindre \| ordinateur \| dans \| seconde |
| Unable to open the e-mail address | Dobertura impossibla de l’adreça electronica | Obertura impossibla de l’adreça electronica | ouvrir |
| Unable to open the workspace settings | Impossible de dobrir los paramètres de l'espaci de trabalh | Impossible d'obrir los paramètres de l'espaci de tribalh | ouvrir \| travail |
| Unable to start new instance of '%s' | Aviada impossibla de l'instància novèla de « %s » | Aviada impossibla de l'instància navèra de « %s » | nouvelle |
| Unnamed Item | Element sens nom | Element shens nom | sans |
| Unnamed item | Element sens nom | Element shens nom | sans |
| Up | Naut | Haut | haut |
| Use c_ustom menu file: | Utilizar un fichièr de menú _personalizat : | Utilizar un fichèr de menú _personalizat : | fichier |
| User ID | ID utilizaire | ID utilizator | utilisateur |
| Username | Nom d’utilizaire | Nom d’utilizator | utilisateur |
| What time is it? | Quina ora es ? | Quina òra ei ? | heure |
| When enabled, all new items will be marked as "Hidden" | Quand es activat, totes los elements novèls son marcats coma « Amagats » | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | comme \| nouveau \| tous |
| Window Menu | Menú de la fenèstra | Menú de la frinèsta | fenetre |
| Window title | Títol de la fenèstra | Títol de la frinèsta | fenetre |
| Workspace %d | Espaci de trabalh %d | Espaci de tribalh %d | travail |
| Workspace Switcher | Cambiador d'espaci de trabalh | Cambiador d'espaci de tribalh | travail |
| Workspace _Settings... | _Preferéncias dels espacis de trabalh... | _Preferéncias deus espacis de tribalh... | des \| travail |
| Wrap around workspaces | Plegar los espacis de trabalh | Plegar los espacis de tribalh | travail |
| You have started X without session manager. Clicking Quit will close the X server. | Avètz aviat lo servidor X sens gestionari de sesilha. En clicant sus Quitar tamparà lo servidor X. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | sans \| session |
| _Add | _Apondre | _Ajustar | ajouter |
| _Arrow button position: | Posicion del boton _flècha : | Posicion deu boton _flècha : | du |
| _Backup and restore | _Salvagardar e restaurar | _Sauvaguardar e restaurar | sauvegarder |
| _Base Directory: | Repertòri de _basa : | Dossièr de _basa : | dossier |
| _Close | _Tampar | _Barrar | fermer |
| _Close All | _Tampar tot | _Barrar tot | fermer |
| _Edit Item | _Editar l'element | _Modificar l'element | modifier |
| _File Pattern: | _Motiu dels fichièrs : | _Motiu deus fichèrs : | des \| fichier |
| _File: | _Fichièr : | _Fichèr : | fichier |
| _Lock Panel | _Varrolhar lo tablèu de bòrd | _Varrolhar lo panèu | panneau |
| _Lock panel | _Varrolhar lo tablèu de bòrd | _Varrolhar lo panèu | panneau |
| _Log Out | _Desconnexion | _Barrar la session | fermer_session |
| _New Game | Jòc _novèl | Jòc _navèth | nouveau |
| _OK | _D'acòrdi | _D'acòrd | accord |
| _Reserve space on screen edges for the panel | _Gardar d’espaci als caires de l’ecran pel panèl | _Gardar d’espaci aus caires de l’ecran entau panèu | aux \| panneau \| pour_le |
| _Restart | _Reamodar | _Tornar aviar | redemarrer |
| _Search: | _Recercar : | _Cercar : | chercher |
| _Show button title | Afichar lo títol del _boton | Afichar lo títol deu _boton | du |
| _Show confirmation dialog | _Afichar una bóstia de dialòg de confirmacion | _Afichar ua bóstia de dialòg de confirmacion | une |
| _Switch User | _Cambiar d'utilizaire | _Cambiar d'utilizator | utilisateur |
| _Switch windows using the mouse wheel | _Cambiar de fenèstra amb l'ajuda de la rodeta de la mirga | _Cambiar de frinèsta dab l'ajuda de la rodeta de la soritz | avec \| fenetre \| souris |
| one | una | ua | une |
| five to %1 | %1 ora manca cinc | %1 òra manca cinc | heure |
| %1 o'clock | %1 ora | %1 òra | heure |
| five to %1 | %1 ora manca cinc | %1 òra manca cinc | heure |
| quarter to %1 | %1 ora manca un quart | %1 òra manca un quart | heure |
| ten to %1 | %1 ora manca dètz | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | heure |
| twenty five to %1 | %1 ora manca vint e cinc | %1 òra manca vint e cinc | heure |
| twenty to %1 | %1 ora manca vint | %1 òra manca vint | heure |
| panels;settings;preferences;taskbar;autohide;application menu;start;buttons;launcher;notification area;status;icons;plugins; | panèls;paramètres;configuracion;reglatges;preferéncias;barra;amagar;rescondre;aplicacions;menú;menut;menu;aviar;aviar;boton;aviador;aviaire;notificacions;estatus;icònas;extensions; | Conservé : Contexte technique ou long : relecture intégrale nécessaire. | panneau |
| one | una | ua | une |
| quarter to %1 | %1 ora manca un quart | %1 òra manca un quart | heure |
| ten to %1 | %1 ora manca dètz | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | heure |
| twenty five to %1 | %1 ora manca vint e cinc | %1 òra manca vint e cinc | heure |
| twenty to %1 | %1 ora manca vint | %1 òra manca vint | heure |

## xfce4-session

| Clé source | Occitan livré | Béarnais retenu ou motif de conservation | Glossaire |
|---|---|---|---|
| (Unknown program) | (Programa desconegut) | (Programa desconeishut) | inconnu |
| (Unknown) | (Desconegut) | (Desconeishut) | inconnu |
| <b>Session Chooser</b> | <b>Seleccion de sesilha</b> | <b>Seleccion de session</b> | session |
| Add application | Apondre una aplicacion | Ajustar ua aplicacion | ajouter \| une |
| All Xfce cache files could not be cleared | L'escondedor fichièrs de Xfce a pas pogut èsser entièrament voidat | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | fichier |
| Always save the session when logging out | Totjorn enregistrar la sesilha quand vos desconnectatz | Totjorn enregistrar la session abans la desconnexion | toujours \| enregistrer \| session \| deconnexion |
| An error occurred | Una error s'es producha | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | une |
| Are you sure you want to empty the session cache? | Sètz segur que volètz voidar l'escondedor de las sesilhas ? | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | session_pluriel \| vider |
| Are you sure you want to terminate "%s"? | Sètz segur que volètz metre fin a « %s » ? | Méter fin a « %s » ? | mettre |
| Automatically save session on logo_ut | _Enregistrar automaticament la sesilha al moment de la desconnexion | _Enregistrar automaticament la session au moment de la desconnexion | au \| session |
| Choose the session you want to restore. You can simply double-click the session name to restore it. | Causir la sesilha que volètz restablir. Podètz simplament doble-clicar sul nom de la sesilha per la restablir. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | session \| sur_le |
| Clear Save_d Sessions | Escafar las sessions enregistra_das | Desfaçar las sessions enregistra_das | effacer |
| Clear sessions | Escafar las sesilhas | Desfaçar las sessions | effacer \| session_pluriel |
| Could not look up internet address for %s.<br>This will prevent Xfce from operating correctly.<br>It may be possible to correct the problem by adding<br>%s to the file /etc/hosts on your system. | Impossible de determinar l'adreça Internet de %s.<br>Aquò geinarà lo bon foncionament de Xfce.<br>Aqueste problèma pòt èsser corregit en apondent<br>%s al fichièr /etc/hosts de vòstre sistèma. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | au \| fichier |
| Create a new session. | Crear una novèla sesilha. | Crear ua navèra session. | nouvelle \| session \| une |
| Current Sessio_n | Sessio_n actuala | Sessio_n actuau | actuel |
| Currently active session: <b>Default</b> | Session activa actuala : <b>Per defaut</b> | Session activa actuau : <b>Per defaut</b> | actuel |
| Customize desktop startup | Personalizar l’aviada del burèu | Personalizar l’aviada deu burèu | du |
| Delete a saved session. | Suprimir una session enregistrada. | Suprimir ua session enregistrada. | une |
| Disable binding to TCP ports | Desactivar la ligason als pòrts TCP | Desactivar la ligason aus pòrts TCP | aux |
| Display the session chooser every time Xfce starts | Afichar una causida de sesilha a cada aviada de Xfce | Afichar ua causida de session a cada aviada de Xfce | session \| une |
| Edit | Editar | Modificar | modifier |
| Edit application | Editar l'aplicacion | Modificar l'aplicacion | modifier |
| Failed adding "%s" | Impossible d'apondre « %s » | Impossible d'ajustar « %s » | ajouter |
| Failed to create file %s | Impossible de crear lo fichièr %s | Impossible de crear lo fichèr %s | fichier |
| Failed to edit item | Impossible d’editar l'element | Impossible d’modificar l'element | modifier |
| Failed to edit item "%s" | Impossible d’editar l'element « %s » | Impossible d’modificar l'element « %s » | modifier |
| Failed to hibernate session | Impossible de metre en ivernacion la sesilha | Impossible de méter en ivernacion la session | mettre \| session |
| Failed to hybrid sleep session | Fracàs del passatge en velha ibrida | Conservé : Sens, accord ou terminologie technique de la source non validés. | du |
| Failed to open %s for reading | Impossible de dobrir %s per la lectura | Impossible d'obrir %s per la lectura | ouvrir |
| Failed to open %s for writing | Impossible de dobrir %s per l'escritura | Impossible d'obrir %s per l'escritura | ouvrir |
| Failed to set run hook | Definicion impossibla del hook d’execucion | Definicion impossibla deu hook d’execucion | du |
| Failed to suspend session | Impossible de metre en velha la sesilha | Impossible de méter en velha la session | mettre \| session |
| Failed to switch user | Cambiament d’utilizaire pas reüssit | Cambiament d’utilizator pas reüssit | utilisateur |
| Failed to write file %s | Impossible d’escriure lo fichièr %s | Impossible d’escríver lo fichèr %s | ecrire \| fichier |
| Halt without displaying the logout dialog | Metre fòra tension sens demandar confirmacion | Méter fòra tension shens demandar confirmacion | mettre \| sans |
| Hibernate without displaying the logout dialog | Metre en ivernacion sens demandar confirmacion | Méter en ivernacion shens demandar confirmacion | mettre \| sans |
| Hybrid Sleep without displaying the logout dialog | Velha ibrida sens afichatge de la fenèstra de desconnexion | Velha ibrida shens afichatge de la frinèsta de desconnexion | fenetre \| sans |
| Last accessed | Darrièr accès | Darrèr accès | derriere |
| Log Out | Desconnexion | Barrar la session | fermer_session |
| Log out %s | Desconnexion de %s | Barrar la session de %s | fermer_session |
| Log out of the Xfce Desktop | Tampar la sesilha del burèu Xfce | Barrar la session deu burèu Xfce | du \| fermer \| session |
| Log out quickly; don't save the session | Desconnexion rapida ; enregistrar pas la sesilha | Barrar la session shens enregistrar | fermer_session \| sans \| enregistrer |
| Log out without displaying the logout dialog | Se desconnectar sens demandar confirmacion | Barrar la session shens demandar confirmacion | fermer_session \| sans |
| Name for the new session | Nom per la session novèla | Nom per la session navèra | nouvelle |
| Never | Pas jamai | Pas jamèi | jamais |
| OK | D'acòrdi | D'acòrd | accord |
| Prompt for confirmation when logging out | Afichar una bóstia de dialòg que demanda confirmacion abans la desconnexion | Afichar ua bóstia de dialòg que demanda confirmacion abans la desconnexion | une |
| Reboot without displaying the logout dialog | Reamodar sens demandar confirmacion | Tornar aviar shens demandar confirmacion | redemarrer \| sans |
| Received error while trying to log out | Error recebuda al moment de la desconnexion | Error recebuda au moment de la desconnexion | au |
| Save Sess_ion | Salvar la ses_ilha | Enregistrar la sess_ion | enregistrer \| session |
| Saving Session | Enregistrament de la sesilha | Enregistrament de la session | session |
| Select a command | Seleccionar una comanda | Seleccionar ua comanda | une |
| Session Manager | Gestionari de sesilhas | Gestionari de sessions | session_pluriel |
| Session Manager Error | Error del gestionari de sesilha | Error deu gestionari de session | du \| session |
| Session Save Error | Error d'enregistrament de sesilha | Error d'enregistrament de session | session |
| Session and Startup | Sesilha e aviada | Session e aviada | session |
| Session manager must be in idle state when requesting a checkpoint | Lo gestionari de sesilha deu èsser en mòde espèra al moment d'una requèsta d'un punt de contraròtle | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | au \| session \| une |
| Session manager must be in idle state when requesting a restart | Lo gestionari de session deu èsser a l’estat de repaus pendent una requèsta de reaviament | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | une |
| Session manager must be in idle state when requesting a shutdown | Lo gestionari de sesilha deu èsser en mòde espèra al moment d'una requèsta de mesa fòra tension | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | au \| session \| une |
| Shut _Down | _Atudar | _Estupar | eteindre |
| Shutdown is blocked by the kiosk settings | La mesa fòra tension es blocada pels paramètres del quiòsque | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | du \| par_les |
| Start GNOME services, such as gnome-keyring | Aviar los servicis GNOME, tals coma gnome-keyring | Aviar los servicis GNOME, tals com gnome-keyring | comme |
| Start KDE services, such as kdeinit | Aviar los servicis KDE, tals coma kdeinit | Aviar los servicis KDE, tals com kdeinit | comme |
| Start an existing session. | Aviar una session existenta. | Aviar ua session existenta. | une |
| Suspend without displaying the logout dialog | Metre en velha sens demandar confirmacion | Méter en velha shens demandar confirmacion | mettre \| sans |
| Switch _User | Cambiar _utilizaire | Cambiar _utilizator | utilisateur |
| Switch user without displaying the logout dialog | Cambiar d’utilizaire sens afichar la fenèstra de desconnexion | Cambiar d’utilizator shens afichar la frinèsta de desconnexion | fenetre \| sans \| utilisateur |
| Terminate Program | Metre fin al programa | Méter fin au programa | au \| mettre |
| The Xfce development team. All rights reserved. | L'equipa de desvolopament Xfce. Totes los dreches reservats. | L'equipa de desvolopament Xfce. Tots los dreches reservats. | tous |
| The application will lose any unsaved state and will not be restarted in your next session. | L'aplicacion va pèrdre tot estat pas salvat e serà pas reaviat dins vòstra sesilha venenta. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | dans \| session |
| The list of applications in the failsafe session is empty. | La lista d'aplicacions de la sesilha sens fracàs es voida. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | sans \| session |
| The saved states of your applications will not be restored during your next login. | L'estat salvat de vòstras aplicacions serà pas restablit al moment de vòstra sesilha venenta. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | au \| session |
| The specified failsafe session ("%s") is not marked as a failsafe session. | La sesilha sens fracàs (« %s ») es pas marcada coma tala. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | comme \| sans \| session |
| These applications are a part of the currently-running session,<br>and can be saved now or when you log out.<br>Changes below will only take effect when the session is saved. | Aquestas aplicacions fan part d’una session actualament en execucion,<br>e pòdon èsser salvadas ara o quand vos desconnectaretz.<br>Las modificacions çai-jos prendràn sonque efièch un còp la session salvada. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | une |
| Unable to create user interface from embedded definition data | Impossible de crear l'interfàcia d'utilizaire a partir de las donadas de definicion embarcats | Conservé : Sens, accord ou terminologie technique de la source non validés. | donnees \| utilisateur |
| Unable to determine failsafe session name.  Possible causes: xfconfd isn't running (D-Bus setup problem); environment variable $XDG_CONFIG_DIRS is set incorrectly (must include "%s"), or xfce4-session is installed incorrectly. | Impossible de determinar lo nom de la sesilha  sens fracàs. Causas possiblas : xfconfd fonciona pas (problèma de configuracion D-Bus); la variabla d'environament $XDG_CONFIG_DIRS es pas definida corrèctament (deu conténer « %s ») ; o xfce4-session es pas installat corrèctament. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | sans \| session |
| Unable to load a failsafe session | Impossible de cargar una sesilha sens fracàs | Conservé : Sens, accord ou terminologie technique de la source non validés. | sans \| session \| une |
| Unable to save the session | Impossible d'enregistrar la sesilha | Impossible d'enregistrar la session | session |
| Unable to terminate program. | Impossible de metre fin al programa. | Impossible de méter fin au programa. | au \| mettre |
| Use this session to run Xfce as your desktop environment | Utilizatz aquesta sesilha per executar Xfce coma environament de burèu | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | comme \| session |
| Xfce Session | Sesilha Xfce | Session Xfce | session |
| You might need to delete some files manually in "%s". | Poiriatz aver besonh de suprimir d'unes fichièrs manualament dins « %s ». | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | dans \| fichier |
| Your session is being saved.  If you do not wish to wait, you may close this window. | Vòstra sesilha es enregistrada. Se volètz pas esperar, podètz tampar aquesta fenèstra. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | fenetre \| fermer \| session |
| _Close | _Tampar | _Barrar | fermer |
| _Display chooser on login | Al moment de l'a_viada, causir una sesilha salvada | Au moment de l'a_viada, causir ua session salvada | au \| session \| une |
| _General | _General | _Generau | general |
| _Log Out | _Desconnexion | _Barrar la session | fermer_session |
| _OK | _D'acòrdi | _D'acòrd | accord |
| _Restart | _Reamodar | _Tornar aviar | redemarrer |
| _Save session for future logins | _Enregistrar la sesilha per las<br>connexions que venon | _Enregistrar la session entà las connexions seguentas | enregistrer \| session \| pour \| connexion |
| on hybrid sleep | en passant al mòde ibrid | en passant au mòde ibrid | au |
| on switch user | en cambiant d’utilizaire | en cambiant d’utilizator | utilisateur |
| session;settings;preferences;manager;startup;login;logout;shutdown;lock screen;application;autostart;launch;services;daemon;agent; | session;settings;preferences;manager;startup;login;logout;shutdown;lock screen;application;autostart;launch;services;daemon;agent;aviar;aviada;atudar;velha;dodo;atudar;reaviar;iber;tampar;tancar: | Conservé : Contexte technique ou long : relecture intégrale nécessaire. | eteindre \| fermer \| redemarrer |

## xfdesktop

| Clé source | Occitan livré | Béarnais retenu ou motif de conservation | Glossaire |
|---|---|---|---|
|     Desktop File Icons:  %s<br> |    Icònas dels fichièrs del burèu :  %s<br> |    Icònas deus fichèrs deu burèu :  %s<br> | des \| du \| fichier |
|     Desktop Icons:       %s<br> |     Icònas del burèu :       %s<br> |     Icònas deu burèu :       %s<br> | du |
|     Desktop Menu:        %s<br> |     Menú del burèu :        %s<br> |     Menú deu burèu :        %s<br> | du |
| %s<br>Size: %s<br>Last modified: %s | %s<br>Talha : %s<br>Darrièra modificacion : %s | %s<br>Talha : %s<br>Darrèra modificacion : %s | derniere |
| (unknown) | (desconegut) | (desconeishut) | inconnu |
| <b>Desktop Menu</b> | <b>Menú del burèu</b> | <b>Menú deu burèu</b> | du |
| <b>Window List Menu</b> | <b>Menú de la lista de la fenèstra</b> | <b>Menú de la lista de la frinèsta</b> | fenetre |
| <b>Workspace %d</b> | <b>Espaci de trabalh %d</b> | <b>Espaci de tribalh %d</b> | travail |
| A normal file with the same name already exists. Please delete or rename it. | Un fichièr normal qu'a lo meteis nom existís ja. Suprimissètz-lo o lo tornar nomenar. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | deja \| fichier \| meme \| normal |
| Advance to the next wallpaper on the current workspace | Avançar cap al fons d’ecran venant sus l’espaci de trabalh actual | Avançar cap au hons d’ecran venant sus l’espaci de tribalh actuau | actuel \| au \| fond \| travail |
| Apply to all _workspaces | Aplicar a totes los espacis de trabalh | Aplicar a tots los espacis de _tribalh | appliquer \| tous \| travail |
| Arrange Desktop _Icons | _Arrengar las icònas del burèu | _Arrengar las icònas deu burèu | du |
| Automatically arrange all the icons on the desktop | Organizar automaticament totas las icònas sul burèu | Organizar automaticament totas las icònas suu burèu | sur_le |
| Automatically select a different background from the current directory. | Seleccionar automaticament un rèire plan diferent dempuèi lo repertòri corrent. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | dossier |
| Bottom Right Horizontal | D’enbàs a la drecha a l’orizontala | D’enbàs a la dreta a l’orizontala | droite |
| Bottom Right Vertical | D’enbàs a drecha a la verticala | D’enbàs a dreta a la verticala | droite |
| Built with GTK+ %d.%d.%d, linked with GTK+ %d.%d.%d. | Construsís amb GTK+ %d.%d.%d, ligat amb GTK+ %d.%d.%d. | Construsís dab GTK+ %d.%d.%d, ligat dab GTK+ %d.%d.%d. | avec |
| Change the _background  | Cambiar lo fons d'ecran | Cambiar lo _hons d'ecran  | fond \| ecran |
| Choose the folder to select wallpapers from. | Causir lo dorsièr que conten los fonzes  d’ecran. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | dossier |
| Copy _Here | _Copiar aicí | _Copiar ací | ici |
| Could not create a new document from the template | Impossible de crear un document novèl dempuèi lo modèl | Impossible de crear un document navèth a partir deu modèle | impossible \| creer \| document \| nouveau \| du \| modele |
| Could not create a new file | Impossible de crear un fichièr novèl | Impossible de crear un fichèr navèth | fichier \| nouveau |
| Could not create the desktop folder "%s" | Impossible de crear lo repertòri del burèu « %s » | Impossible de crear lo dossièr deu burèu « %s » | dossier \| du |
| Could not empty the trash | Impossible de voidar l'escobilhièr | Impossible de vueitar l'escobilhièr | vider |
| Create Document Error | Error de creacion del document | Error de creacion deu document | du |
| Create File Error | Error de creacion del fichièr | Error de creacion deu fichèr | du \| fichier |
| Create _Folder... | Crear un _dorsièr... | Crear un _dossièr... | dossier |
| Desktop Folder Error | Error dins lo repertòri del burèu | Error dens lo dossièr deu burèu | dans \| dossier \| du |
| Desktop Settings | Paramètres del burèu | Paramètres deu burèu | du |
| Desktop _Settings... | Paramètres del _burèu... | Paramètres deu _burèu... | du |
| Do you really want to remove workspace %d?<br>Note: You are currently on workspace %d. | Sètz segur que volètz suprimir l'espaci de trabalh %d<br>Remarca : Actualament, sètz sus l'espaci de trabalh %d. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | travail |
| Do you really want to remove workspace '%s'?<br>Note: You are currently on workspace '%s'. | Sètz segur que volètz suprimir l'espaci de trabalh « %s »<br>Remarca : Actualament, sètz sus l'espaci de trabalh « %s ». | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | travail |
| Ejecting device | Ejeccion del periferic | Ejeccion deu periferic | du |
| Enable "Delete" option in file context menu | Activar l’opcion « Suprimir » al menú contextual fichièr | Activar l’opcion « Suprimir » au menú contextual fichèr | au \| fichier |
| Failed to load the desktop folder | Impossible de cargar lo repertòri del burèu | Impossible de cargar lo dossièr deu burèu | dossier \| du |
| Failed to parse arguments: %s<br> | Fracàs de l'analisi dels arguments : %s<br> | Fracàs de l'analisi deus arguments : %s<br> | des |
| File Properties Error | Error de proprietats de fichièr | Error de proprietats de fichèr | fichier |
| File System | Sistèma de fichièrs | Sistèma de fichèrs | fichier |
| File/launcher icons | Icònas fichièr / aviador | Icònas fichèr / aviador | fichier |
| Home | Repertòri personal | Dossièr personau | dossier \| personnel |
| Image files | Fichièrs imatges | Fichèrs imatges | fichier |
| Launch Error | Error al moment de l'aviada | Error au moment de l'aviada | au |
| Mo_ve to Trash | Desplaçar  dins l'escobilhièr | Desplaçar dens l'_escobilhièr | deplacer \| dans |
| Move this dialog to the display and workspace you want to edit the settings for. | Desplaçar aquesta fenèstra cap a l’ecran e espaci de trabalh que volètz modificar los paramètres. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | fenetre \| travail |
| Move this dialog to the display you want to edit the settings for. | Desplaçar aquesta fenèstra cap a l’ecran que volètz modificar los paramètres. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | fenetre |
| Move this dialog to the workspace you want to edit the settings for. | Desplaçar aquesta bóstia de dialòg cap a l'espaci de trabalh que ne volètz modificar los paramètres. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | travail |
| Name: %s<br>Type: %s<br>Size: %s<br>Last modified: %s | Nom : %s<br>Tipe : %s<br>Talha : %s<br>Darrièra modificacion : %s | Nom : %s<br>Tipe : %s<br>Talha : %s<br>Darrèra modificacion : %s | derniere |
| No templates installed | Cap de modèl pas installat | Cap de modèle pas installat | modele |
| Open With | Dobrir amb | Obrir dab | avec \| ouvrir |
| Open With "%s" | Dobrir amb « %s » | Obrir dab « %s » | avec \| ouvrir |
| Open With Other _Application... | Dobrir amb una autra _aplicacion... | Obrir dab ua auta _aplicacion... | autre \| avec \| ouvrir \| une |
| Other Devices | Autres periferics | Autes periferics | autres |
| Paste Into Folder | Pegar dins lo dorsièr | Pegar dens lo dossièr | dans \| dossier |
| Pop up the menu (at the current mouse position) | Far aparéisser lo menú (a la posicion actuala de la mirga) | Har aparéisser lo menú (a la posicion actuau de la soritz) | actuel \| faire \| souris |
| Pop up the window list (at the current mouse position) | Far aparéisser la lista de las fenèstras (a la posicion correnta de la mirga) | Conservé : Flexion nouvelle non attestée dans les sources consultées. | faire \| souris |
| Randomly selects another image from the same directory when the wallpaper is to cycle. | Seleccionar aleatòriament un autre imatge del meteis repertòri quand lo papièr pintrat es del cicle. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | autre \| dossier \| du \| meme |
| Reload all settings | Recargar totes los paramètres | Recargar tots los paramètres | tous |
| Remove Workspace %d | Suprimir l'espaci de trabalh %d | Suprimir l'espaci de tribalh %d | travail |
| Remove Workspace '%s' | Suprimir l'espaci de trabalh « %s » | Suprimir l'espaci de tribalh « %s » | travail |
| Right | Alinhat a drecha | Alinhat a dreta | droite |
| Select First Color | Seleccionar la primièra color | Seleccionar la purmèra color | premiere |
| Select a Directory | Seleccionar un Repertòri | Seleccionar un Dossièr | dossier |
| Select this option to display preview-able files on the desktop as automatically generated thumbnail icons. | Seleccionatz aquesta opcion per representar los fichièrs imatges o vidèos sul burèu jos forma d'icònas vinhetas generadas automaticament. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | fichier \| sur_le \| video |
| Set desktop background and menu and icon behavior | Reglar lo fons d'ecran del burèu, lo menú e lo comportament de las icònas | Reglar lo hons d'ecran deu burèu, lo menú e lo comportament de las icònas | du \| fond |
| Settings manager socket | Socket del gestionari de paramètres | Socket deu gestionari de paramètres | du |
| Sh_ow application icons in menu | Afichar las icònas _de las aplicacions dins lo menú | Afichar las icònas _de las aplicacions dens lo menú | dans |
| Show _application icons in menu | Afichar _las icònas de las aplicacions dins lo menú | Afichar _las icònas de las aplicacions dens lo menú | dans |
| Show _window list menu on desktop middle click | Afichar lo menú que fa la lista de las fenès_tras al moment d'un clic mitan sul burèu | Conservé : Flexion nouvelle non attestée dans les sources consultées. | au \| sur_le |
| Show a_dd and remove workspace options in list | Afichar las opcions a_pondre e suprimir d’espacis de trabalh a la lista | Afichar las opcions _ajustar e suprimir d’espacis de tribalh a la lista | ajouter \| travail |
| Show hidden files on the desktop | Afichar los fichièrs amagats pel burèu | Afichar los fichèrs amagats pel burèu | fichier |
| Show s_ticky windows only in active workspace | Far la lista de las fenèstras _pegantas unicament dins l'espaci de trabalh actiu | Conservé : Flexion nouvelle non attestée dans les sources consultées. | dans \| faire \| travail |
| Show workspace _names in list | Afichar los _noms dels espacis de trabalh dins la lista | Afichar los _noms deus espacis de tribalh dens la lista | dans \| des \| travail |
| Specifies the "right" or "bottom" color of the gradient. | Especifica la color unida, o aquela de drech o d’enbàs del degradat. | Especifica la color unida, o aquela de drech o d’enbàs deu degradat. | du |
| Specifies the solid color, or the "left" or "top" color of the gradient. | Especifica la color unida, o aquela d’esquèrra o d’ennaut del degradat. | Especifica la color unida, o aquela d’esquèrra o d’ennaut deu degradat. | du |
| Specify how often the background will change. | Especificar la frequéncia que lo fons d’ecran cambiarà. | Especificar la frequéncia que lo hons d’ecran cambiarà. | fond |
| Specify the style of the color drawn behind the backdrop image. | Especificar l’estil de la color ajustada darrièr l’imatge de fons. | Especificar l’estil de la color ajustada darrèr l’imatge de hons. | derriere \| fond |
| The Xfce development team. All rights reserved. | L'equipa de desvolopament Xfce. Totes los dreches reservats. | L'equipa de desvolopament Xfce. Tots los dreches reservats. | tous |
| The device "%s" has been safely removed from the system.  | Lo periferic « %s » es estat levat en tota seguretat del sistèma. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | du |
| The device "%s" is being unmounted by the system. Please do not remove the media or disconnect the drive | Lo periferic « %s » es en cors de desmontatge pel sistèma. Levetz pas lo supòrt o desconnectetz pas lo lector. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | par_le |
| The file could not be opened | Lo fichièr a pas pogut èsser dobèrt | Impossible d'obrir lo fichèr | impossible \| ouvrir \| fichier |
| The file could not be renamed | Lo fichièr a pas pogut èsser renomenada | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | fichier |
| The file properties dialog could not be opened | La bóstia de dialòg de las proprietats del fichièr a pas pogut èsser dobèrt | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | du \| fichier |
| The file transfer could not be performed | Lo transferiment de fichièr a pas pogut èsser efectuat | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | fichier |
| The files could not be renamed | Los fichièrs pòdon pas èsser renomenats | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | fichier |
| The folder could not be opened | Lo repertòri a pas pogut èsser dobèrt | Impossible d'obrir lo dossièr | impossible \| ouvrir \| dossier |
| The selected files could not be deleted | Los fichièrs seleccionats an pas pogut èsser suprimits | Impossible de suprimir los fichèrs seleccionats | impossible \| supprimer \| fichier |
| The selected files could not be moved to the trash | Los fichièrs seleccionats an pas pogut èsser desplaçats dins l'escobilhièr | Impossible de desplaçar los fichèrs seleccionats dens l'escobilhièr | impossible \| deplacer \| fichier \| dans |
| There is data that needs to be written to the device "%s" before it can be removed. Please do not remove the media or disconnect the drive | De donadas devon èsser escrichas sul periferic « %s » abans sa desconnexion. Levetz pas lo supòrt o desconnectetz pas lo lector. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | donnees \| sur_le |
| This feature requires a file manager service to be present (such as the one supplied by Thunar). | Aquesta foncionalitat requerís la preséncia d'un gestionari de fichièrs (coma Thunar). | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | comme \| fichier |
| This feature requires a trash service to be present (such as the one supplied by Thunar). | Aquesta foncionalitat requesís la preséncia d'un servici d'escobilhièr (tal coma lo qu'es provesit per Thunar). | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | comme |
| This will reorder all desktop items and place them on different screen positions.<br>Are you sure? | Aquò reordenarà totes los elements del burèu e los botarà dins diferentas posicion de l’ecran.<br>O volètz vertadièrament ? | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | dans \| du \| tous |
| Today at %X | Uèi a %X | Uei a %X | aujourdhui |
| Top Right Horizontal | D’ennaut a drecha a l’orizontala | D’ennaut a dreta a l’orizontala | droite |
| Top Right Vertical | D’ennaut a drecha a la verticala | D’ennaut a dreta a la verticala | droite |
| Trash is empty | Escobilhièr void | Escobilhièr vueit | vide |
| Unable to launch "exo-desktop-item-edit", which is required to create and edit launchers and links on the desktop. | Impossible d'aviar « exo-desktop-item-edit », qu'es necessari a la creacion e l'edicion dels aviadors e dels ligams sul burèu. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | des \| sur_le |
| Unknown | Desconegut | Desconeishut | inconnu |
| Unmounting device | Desmontatge del periferic | Desmontatge deu periferic | du |
| Untitled document | Document sens nom | Document shens nom | sans |
| Use _submenus for the windows in each workspace | Utilizar de _sosmenús per cada espaci de trabalh | Utilizar de _sosmenús per cada espaci de tribalh | travail |
| Use custom _font size: | Utilizar una talha de _poliça personalizada : | Conservé : Sens, accord ou terminologie technique de la source non validés. | police \| une |
| Wallpaper for %s | Fons d'ecran per %s | Hons d'ecran per %s | fond |
| Wallpaper for %s on Monitor %d | Fons d'ecran per %s sul monitor %d | Hons d'ecran per %s suu monitor %d | fond \| sur_le |
| Wallpaper for %s on Monitor %d (%s) | Fons d'ecran per %s sul monitor %d (%s) | Hons d'ecran per %s suu monitor %d (%s) | fond \| sur_le |
| Wallpaper for Monitor %d | Fons d'ecran pel monitor %d  | Hons d'ecran entau monitor %d  | fond \| pour_le |
| Wallpaper for Monitor %d (%s) | Fons d'ecran pel monitor %d (% s) | Conservé : Paramètres de substitution divergents dans la source : correction complète nécessaire. | fond \| pour_le |
| Wallpaper for my desktop | Fons d'ecran per mon burèu | Hons d'ecran per mon burèu | fond |
| Writing data to device | Escritura de las donadas sul periferic | Escritura de las dadas suu periferic | donnees \| sur_le |
| Yesterday at %X | Ièr a %X | Ger a %X | hier |
| _Add Workspace | _Apondre un espaci de trabalh | _Ajustar un espaci de tribalh | ajouter \| travail |
| _Background | _Fons d'ecran | _Hons d'ecran | fond |
| _Close | _Tampar | _Barrar | fermer |
| _Edit Launcher | _Editar l'aviador | _Modificar l'aviador | modifier |
| _Edit desktop menu | Editar lo _menú del burèu | Modificar lo _menú deu burèu | du \| modifier |
| _Empty File | _Fichièr void | _Fichèr vueit | fichier \| vide |
| _Empty Trash | _Voidar l'escobilhièr | _Vueitar l'escobilhièr | vider |
| _Folder: | Dorsièr : | Conservé : Nombre de raccourcis divergent dans la source : correction contextualisée nécessaire. | dossier |
| _Link Here | _Ligar aicí | _Ligar ací | ici |
| _Lock Volume | _Verrolhar lo volum | _Varrolhar lo volum | verrouiller |
| _Move Here | _Desplaçar aicí | _Desplaçar ací | ici |
| _Next Background | Fons d’ecran _seguent | Hons d’ecran _seguent | fond |
| _OK | _D'acòrdi | _D'acòrd | accord |
| _Open | _Dobrir | _Obrir | ouvrir |
| _Open With "%s" | _Dobrir amb « %s » | _Obrir dab « %s » | avec \| ouvrir |
| _Open all | _Dobrir totes | _Obrir tots | ouvrir \| tous |
| _Open in New Window | _Dobrir dins una novèla fenèstra | _Obrir dens ua navèra frinèsta | dans \| fenetre \| nouvelle \| ouvrir \| une |
| _Random Order | Òrdre aleatòri | Conservé : Nombre de raccourcis divergent dans la source : correction contextualisée nécessaire. | ordre |
| _Remove Workspace %d | _Suprimir l'espaci de trabalh %d | _Suprimir l'espaci de tribalh %d | travail |
| _Remove Workspace '%s' | _Suprimir l'espaci de trabalh « %s » | _Suprimir l'espaci de tribalh « %s » | travail |
| _Window Actions | _Accions de la fenèstra | _Accions de la frinèsta | fenetre |
| every day | cada jorn | cada dia | jour |
| every hour | cada ora | cada òra | heure |
| in hours: | en oras : | en òras : | heure |

## thunar

| Clé source | Occitan livré | Béarnais retenu ou motif de conservation | Glossaire |
|---|---|---|---|
| A destination directory must be specified | Un repertòri de destinacion deu èsser especificat | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | dossier |
| About Templates | A prepaus dels modèls | A prepaus deus modèles | des \| modele |
| Acquired the name '%s' on the session message bus<br> | Nom « %s » obtengut sul bus de messatge session<br> | Nom « %s » obtengut suu bus de messatge session<br> | sur_le |
| Add a new custom action. | Apondre una novèla accion personalizada. | Ajustar ua navèra accion personalizada. | ajouter \| nouvelle \| une |
| All Files | Totes los fichièrs | Tots los fichèrs | fichier \| tous |
| All files in this folder will appear in the "Create Document" menu. | Totes los fichièrs dins aqueste dorsièr apareisseràn dins lo menú « Crear un document » | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | dans \| dossier \| fichier \| tous |
| Allow this file to _run as a program | Autorizar aqueste fichièr a èsser _executat coma un programa | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | comme \| fichier |
| Aperture Value: | Valor de dobertura : | Valor de obertura : | ouvrir |
| Apply to Folder Only | Aplicar al dorsièr unicament | Aplicar au dossièr unicament | au \| dossier |
| Apply to Folder and Contents | Aplicar al dorsièr e son contengut | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | au \| contenu \| dossier |
| Are you sure you want to open all folders? | Sètz segur que volètz dobrir totes los dorsièrs ? | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | dossier \| ouvrir \| tous |
| At least one filename must be specified | Al mens un fichièr deu èsser especificat | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | au \| fichier \| moins |
| At least one source filename must be specified | Al mens un fichièr font deu èsser especificat | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | au \| fichier \| moins \| source |
| Audio Files | Fichièrs àudio | Fichèrs àudio | fichier |
| Authentication is required to run Thunar as root. | Una autentificacion es requesida per aviar Thunar en tant que root. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | une |
| Browse Network | Percórrer la ret | Percórrer lo hialat | reseau |
| Browse local network connections | Percórrer las connexions de la ret locala | Percórrer las connexions deu hialat locau | connexion \| du \| reseau |
| Browse recently used files | Percórrer los fichièrs recentament utilizats | Percórrer los fichèrs recentament utilizats | fichier |
| Browse the computer | Percórrer l’ordenador | Percórrer l’ordinator | ordinateur |
| Browse the file system | Percórrer lo sistèma de fichièrs | Percórrer lo sistèma de fichèrs | fichier |
| Browse the file system to select an application to open files of type "%s". | Percórrer lo sistèma de fichièrs per seleccionar una aplicacion per dobrir los fichièrs de tipe « %s ». | Percórrer lo sistèma de fichèrs per seleccionar ua aplicacion per obrir los fichèrs de tipe « %s ». | fichier \| ouvrir \| une |
| Browse the file system to select an application to use for this action. | Percórrer lo sistèma de fichièrs per seleccionar una aplicacion d'utilizar per aquesta accion. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | fichier \| une |
| Browse the filesystem with the file manager | Percórrer lo sistèma de fichièrs amb lo gestionari de fichièrs | Percórrer lo sistèma de fichèrs dab lo gestionari de fichèrs | avec \| fichier |
| Bulk Rename - Rename Multiple Files | Renomenar en massa - Renomenar mantun fichièr | Renomenar en massa - Renomenar mantun fichèr | fichier |
| By default columns will be automatically expanded if<br>needed to ensure the text is fully visible. If you dis-<br>able this behavior below the file manager will always<br>use the user defined column widths. | Per defaut, las colomnas son automaticament alargidas per que la totalitat del tèxte siá visible. Desmarcatz la casa per que las colomnas conserven totjorn las largors definidas per l'utilizaire. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | du \| utilisateur |
| C_lose Tab | _Tampar l'onglet | _Barrar l'onglet | fermer |
| Camera Model: | Modèl de l'aparelh : | Modèle de l'aparelh : | modele |
| Cancel search for files | Anullar la recèrca de fichièrs | Anullar la recèrca de fichèrs | fichier |
| Cannot convert filename "%s" to the local encoding | Pòt pas convertir lo nom del fichièr « %s » cap a l'encodatge local | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | du \| fichier |
| Change the default application for files of type "%s" to the selected application. | Modificar l'aplicacion per defaut pels fichièrs de tipe « %s » per l'aplicacion seleccionada. | Modificar l'aplicacion per defaut entaus fichèrs de tipe « %s » per l'aplicacion seleccionada. | fichier \| pour_les |
| Change the visibility of this window's menubar | Cambiar la visibilitat de la barra de menú d'aquesta fenèstra | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | fenetre |
| Change the visibility of this window's statusbar | Cambiar la visibilitat de la barra d'estatut de la fenèstra | Cambiar la visibilitat de la barra d'estatut de la frinèsta | fenetre |
| Choose an application which should be used by default to open the selected file | Causissètz una aplicacion amb la quala cal dobrir lo fichièr seleccionat per defaut | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | avec \| fichier \| ouvrir \| une |
| Choose another application with which to open the selected file | Causissètz una autra aplicacion amb la quala cal dobrir lo fichièr seleccionat | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | autre \| avec \| fichier \| ouvrir \| une |
| Choose the order of information to appear in the<br>detailed list view. | Causir l'òrdre de las informacions a paréisser dins<br>l'afichatge de la lista detalhada. | Causir l'òrdi de las informacions a paréisser dens<br>l'afichatge de la lista detalhada. | dans \| ordre |
| Clear | Escafar | Desfaçar | effacer |
| Clear the file list below | Voidar la lista de fichièr çaijós | Vueitar la lista de fichèrs ací devath | vider \| liste \| fichier \| dessous_ici |
| Click here to automatically fix the folder permissions. | Clicar aicí per corregir automaticament los dreches del dorsièr. | Clicar ací per corregir automaticament los dreches deu dossièr. | dossier \| du \| ici |
| Click here to stop calculating the total size of the folder. | Clicatz aicí per arrestar lo calcul de la talha totala del dorsièr. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | dossier \| du \| ici |
| Click here to view the documentation for the selected rename operation. | Clicatz aicí per consultar la documentacion per l'operacion de cambiament de nom seleccionada. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | ici |
| Click this button to select an icon file that will be displayed in the context menu in addition to the action name chosen above. | Clicatz sus aqueste boton per seleccionar l'icòna qu'apareisserà dins lo menú contextual en mai del nom de l'accion causit en dessús. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | dans \| du \| plus |
| Close _All Windows | Tampar _totas las fenèstras | Conservé : Flexion nouvelle non attestée dans les sources consultées. | fermer |
| Close all Thunar windows | Tampar totas las fenèstras de Thunar | Conservé : Flexion nouvelle non attestée dans les sources consultées. | fermer |
| Close tab | Tampar l'onglet | Barrar l'onglet | fermer |
| Close this folder | Tampar aqueste repertòri | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | dossier \| fermer |
| Close this window | Tampar aquesta fenèstra | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | fenetre \| fermer |
| Collecting files... | Recuperacion dels fichièrs... | Recuperacion deus fichèrs... | des \| fichier |
| Compact directory listing | Lista compacta dels repertòris | Lista compacta deus dossièrs | des \| dossier |
| Compressing files... | Compression dels fichièrs... | Compression deus fichèrs... | des \| fichier |
| Configure Columns in the Detailed List View | Configurar las colomnas dins la Lista detalhada | Configurar las colomnas dens la Lista detalhada | dans |
| Configure the Thunar file manager | Configurar lo gestionari de fichièrs Thunar | Configurar lo gestionari de fichèrs Thunar | fichier |
| Confirm to replace files | Confirmar lo remplaçament dels fichièrs | Confirmar lo remplaçament deus fichèrs | des \| fichier |
| Content: | Contengut : | Contiengut : | contenu |
| Copying files to "%s"... | Còpia dels fichièrs dins « %s »... | Còpia deus fichèrs dens « %s »... | dans \| des \| fichier |
| Copying files... | Còpia dels fichièrs... | Còpia deus fichèrs... | des \| fichier |
| Correct _folder permissions | Corregir los dreches del dorsièr | Conservé : Nombre de raccourcis divergent dans la source : correction contextualisée nécessaire. | dossier \| du |
| Correct _folder permissions... | Corregir los dreches del dorsièr... | Conservé : Nombre de raccourcis divergent dans la source : correction contextualisée nécessaire. | dossier \| du |
| Correct folder permissions automatically? | Corregir los dreches del dorsièr automaticament ? | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | dossier \| du |
| Could not delete file "%s": %s | Impossible de suprimir lo fichièr « %s » : %s | Impossible de suprimir lo fichèr « %s » : %s | fichier |
| Could not move "%s" directly. Collecting files for copying... | Impossible de desplaçar « %s » dirèctament. Collècta de fichièrs per èsser copiats ... | Conservé : Sens, accord ou terminologie technique de la source non validés. | fichier |
| Create Action | Crear una accion | Crear ua accion | une |
| Create Document from template "%s" | Crear un document amb lo modèl « %s » | Crear un document dab lo modèle « %s » | avec \| modele |
| Create File | Crear un fichièr | Crear un fichèr | fichier |
| Create Folder | Crear un dorsièr | Crear un dossièr | dossier |
| Create New File | Crear un fichièr novèl | Crear un fichèr navèth | fichier \| nouveau |
| Create New Folder | Crear un dorsièr novèl | Crear un dossièr navèth | dossier \| nouveau |
| Create _Folder... | Crear un _dorsièr... | Crear un _dossièr... | dossier |
| Create a new document from a template | Crear un document novèl a partir d’un modèl | Crear un document navèth a partir d’un modèle | modele \| nouveau |
| Create an empty folder within the current folder | Crèa un dorsièr void dins lo dorsièr corrent | Crear un dossièr vueit dens lo dossièr corrent | creer \| dossier \| vide \| dans |
| Create bookmarks for all selected folders. If nothing is selected, the current folder is bookmarked. | Crear de marcapaginas per totes los dorsièrs seleccionats. Se res es pas seleccionat, lo dorsièr actual serà mes en favorit. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | actuel \| dossier \| tous |
| Create directory | Crear un repertòri | Crear un dossièr | dossier |
| Creating directories... | Creacion dels dorsièrs... | Creacion deus dossièrs... | des \| dossier |
| Creating files... | Creacion dels fichièrs... | Creacion deus fichèrs... | des \| fichier |
| Creating symbolic links in "%s"... | Creacion de ligams simbolics dins « %s » ... | Creacion de ligams simbolics dens « %s » ... | dans |
| Delete all files and folders in the Trash | Suprimís totes los fichièrs e dorsièrs de l'escobilhièr | Suprimir tots los fichèrs e dossièrs de l'escobilhièr | supprimer \| tous \| fichier \| dossier |
| Deleting files... | Supression dels fichièrs... | Supression deus fichèrs... | des \| fichier |
| Detailed directory listing | Lista detalhada dels repertòris | Lista detalhada deus dossièrs | des \| dossier |
| Display Thunar user manual | Afichar lo manual utilizaire de Thunar | Afichar lo manuau utilizator de Thunar | manuel \| utilisateur |
| Display folder content in a compact list view | Aficha lo contengut del dorsièr amb una lista compacta | Afichar lo contiengut deu dossièr en lista compacta | afficher \| contenu \| du \| dossier \| liste |
| Display folder content in a detailed list view | Aficha lo contengut del dorsièr jos la forma de lista detalhada | Afichar lo contiengut deu dossièr en lista detalhada | afficher \| contenu \| du \| dossier \| liste |
| Display folder content in an icon view | Aficha lo contengut del dorsièr jos la forma d'icònas | Afichar lo contiengut deu dossièr dab icònas | afficher \| contenu \| du \| dossier \| avec \| icone |
| Display information about Thunar Bulk Rename | Aficha d'informacions a prepaus de l'aisina Thunar « Renomenar en massa » | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | outil |
| Display recently used files | Afichar los fichièrs recentament utilizats | Afichar los fichèrs recentament utilizats | fichier |
| Display the contents of the trash can | Afichar lo contengut de l'escobilhièr | Afichar lo contiengut de l'escobilhièr | contenu |
| Do _not ask me again | _Me pausar pas mai aquesta question | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | plus |
| Do _not display this message again | A_fichar pas mai aqueste message | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | plus |
| Do you want to apply your changes recursively to<br>all files and subfolders below the selected folder? | Volètz aplicar vòstres cambiaments recursivament<br>a totes los fichièrs e sosdorsièrs del dorsièr seleccionat ? | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | dossier \| du \| fichier \| tous |
| Do you want to replace the existing file | Volètz remplaçar lo fichièr existent | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | fichier |
| Do you want to replace the existing folder | Volètz remplaçar lo dorsièr existent | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | dossier |
| Do you want to skip this file and continue to rename the remaining files? | Volètz ignorar aqueste fichièr e contunhar de renomenar los fichièrs restants ? | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | fichier |
| Draw frames around thumbnails | Dessenhar una bordadura a l'entorn de las miniaturas | Dessenhar ua bordadura a l'entorn de las miniaturas | une |
| Edit Action | Editar l'accion | Modificar l'accion | modifier |
| Edit Thunars Preferences | Editar las preferéncias de Thunar | Modificar las preferéncias de Thunar | modifier |
| Edit the currently selected action. | Editar l'accion actualament seleccionada. | Modificar l'accion actualament seleccionada. | modifier |
| Ejecting device | Ejeccion del periferic | Ejeccion deu periferic | du |
| Empty Trash | Voidar l’escobilhièr | Vueitar l’escobilhièr | vider |
| Enable this option if you want a waiting cursor to be shown while the action is launched. This is also highly recommended if you have focus stealing prevention enabled in your window manager. | Activatz aquesta opcion per afichar un sablièr a l'aviada de l'accion. Aquesta opcion es recomandada se avètz activada la prevencion del vòl del focus dins vòstre gestionari de fenèstras. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | dans \| du |
| Enter a list of patterns that will be used to determine whether this action should be displayed for a selected file. If you specify more than one pattern here, the list items must be separated with semicolons (e.g. *.txt;*.doc). | Entratz una lista de modèls que seràn utilizats per determinar se aquesta accion deu èsser afichada per un fichièr seleccionat. Se especificatz mai d'un modèl aicí, los elements de la lista devon èsser separats per de punts-virgulas (p. e. *.txt,. *.doc). | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | fichier \| ici \| modele \| plus \| une |
| Enter the new name: | Entrar lo novèl nom : | Entrar lo navèth nom : | nouveau |
| Enter the text that should be used as replacement for the pattern above. | Entrar lo tèxte que deu èsser utilizat coma remplaçament pel modèl çaisús. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | comme \| modele |
| Enter the text to search for in the file names. | Entratz lo tèxte de recercar dins los noms de fichièrs. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | chercher \| dans \| fichier |
| Error removing file: %s | Error de supression fichièr : %s | Error de supression fichèr : %s | fichier |
| Error while copying to "%s": %s more space is required to copy to the destination | Error al moment de la còpia cap a « %s » : %s mai d'espaci es necessari per copiar cap a la destinacion | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | au \| plus |
| Example for a custom action | Exemple d'una accion personalizada | Exemple d'ua accion personalizada | une |
| Executable Files | Fichièrs executables | Fichèrs executables | fichier |
| Failed to add new application "%s" | Impossible d'apondre la novèla aplicacion « %s » | Impossible d'ajustar la navèra aplicacion « %s » | ajouter \| nouvelle |
| Failed to add new shortcut | Impossible d'apondre un acorchi novèl | Impossible d'ajustar un acorchi navèth | ajouter \| nouveau |
| Failed to browse the network | Impossible de percórrer la ret | Impossible de percórrer lo hialat | impossible \| reseau |
| Failed to compose new email | Impossible de compausar un novèl email | Impossible de compausar un navèth email | nouveau |
| Failed to create directory "%s": %s | Impossible de crear lo repertòri « %s » : %s | Impossible de crear lo dossièr « %s » : %s | dossier |
| Failed to create empty file "%s": %s | Impossible de crear lo fichièr void « %s » : %s | Impossible de crear lo fichèr vueit « %s » : %s | fichier \| vide |
| Failed to create temporary directory | Impossible de crear lo dorsièr temporari | Impossible de crear lo dossièr temporari | dossier |
| Failed to display the contents of the trash can | Impossible d'afichar lo contengut de l'escobilhièr | Impossible d'afichar lo contiengut de l'escobilhièr | contenu |
| Failed to execute file "%s" | Impossible d'executar lo fichièr « %s » | Impossible d'executar lo fichèr « %s » | fichier |
| Failed to open "%s" | Impossible de dobrir « %s » | Impossible d'obrir « %s » | ouvrir |
| Failed to open "%s": %s | Impossible de dobrir « %s » : %s | Impossible d'obrir « %s » : %s | ouvrir |
| Failed to open directory "%s" | Impossible de dobrir lo repertòri « %s » | Impossible d'obrir lo dossièr « %s » | dossier \| ouvrir |
| Failed to open file "%s" | Impossible de dobrir lo fichièr « %s » | Impossible d'obrir lo fichèr « %s » | fichier \| ouvrir |
| Failed to open parent folder | Impossible de dobrir lo dorsièr parent | Impossible d'obrir lo dossièr parent | dossier \| ouvrir |
| Failed to open the documentation browser | Impossible de dobrir lo navigador de documentacion | Impossible d'obrir lo navigador de documentacion | ouvrir |
| Failed to open the file system root folder | Impossible de dobrir lo dorsièr raiç del sistèma de fichièrs | Impossible d'obrir lo dossièr raiç deu sistèma de fichèrs | dossier \| du \| fichier \| ouvrir |
| Failed to open the home folder | Impossible de dobrir lo dorsièr personal | Impossible d'obrir lo dossièr personau | dossier \| ouvrir \| personnel |
| Failed to parse the desktop file: %s | Impossible d'analisar lo fichièr del burèu : « %s » | Impossible d'analisar lo fichèr deu burèu : « %s » | du \| fichier |
| Failed to restore the folder "%s" | Impossible de restablir lo dorsièr « %s » | Impossible de restablir lo dossièr « %s » | dossier |
| Failed to save "%s". | Impossible de salvar « %s » | Impossible de enregistrar « %s » | enregistrer |
| Failed to save actions to disk. | Impossible de salvar d'accions sul disc. | Impossible de enregistrar d'accions suu disc. | enregistrer \| sur_le |
| File | Fichièr | Fichèr | fichier |
| File Manager | Gestionari de fichièrs | Gestionari de fichèrs | fichier |
| File Manager Preferences | Preferéncias del gestionari de fichièrs | Preferéncias deu gestionari de fichèrs | du \| fichier |
| File Manager Settings | Paramètres del gestionari de fichièrs | Paramètres deu gestionari de fichèrs | du \| fichier |
| File Name | Nom del fichièr | Nom deu fichèr | du \| fichier |
| File Operation Progress | Fichièr en cors de tractament | Fichèr en cors de tractament | fichier |
| File System | Sistèma de fichièrs | Sistèma de fichèrs | fichier |
| File Transfer | Transferiment de fichièrs | Transferiment de fichèrs | fichier |
| File does not exist | Lo fichièr existís pas | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | fichier |
| Filetype | Tipe de fichièr | Tipe de fichèr | fichier |
| First character uppercase | Primièra letra en majuscula | Purmèra letra en majuscula | premiere |
| Flash Fired: | Utilizacion del flash : | Utilizacion deu flash : | du |
| Focal Length: | Longor del focus : | Longor deu focus : | du |
| Folder Permissions | Permissions del dorsièr | Permissions deu dossièr | dossier \| du |
| Folder permissions | Permissions del dorsièr | Permissions deu dossièr | dossier \| du |
| Free space: %s | Espaci liure : %s | Espaci libre : %s | libre |
| From the back (right) | A partir de drecha | A partir de dreta | droite |
| General | General | Generau | general |
| Go to the desktop folder | Anar al dorsièr del burèu | Anar au dossièr deu burèu | au \| dossier \| du |
| Go to the home folder | Anar al dorsièr personal | Anar au dossièr personau | au \| dossier \| personnel |
| Go to the next visited folder | Anar cap al dorsièr visitat seguent | Anar cap au dossièr visitat seguent | au \| dossier |
| Go to the previous visited folder | Anar cap al dorsièr visitat precedent | Anar cap au dossièr visitat precedent | au \| dossier |
| Go to the templates folder | Anar cap al dorsièr dels modèls | Anar cap au dossièr deus modèles | au \| des \| dossier \| modele |
| Home | Repertòri personal | Dossièr personau | dossier \| personnel |
| Icon based directory listing | Lista dels repertòris jos la fòrma d'icònas | Lista deus dossièrs jos la fòrma d'icònas | des \| dossier |
| If you choose to empty the Trash, all items in it will be permanently lost. Please note that you can also delete them separately. | Voidar l'escobilhièr suprimirà definitivament totes los elements que s'i tròban. Aqueles darrièrs pòdon èsser escafats separadament. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | tous \| vider |
| If you delete a custom action, it is permanently lost. | Se suprimissètz una accion personalizada, es definitivament perduda. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | une |
| If you delete a file, it is permanently lost. | Se suprimissètz aqueste fichièr, serà perdut definitivament. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | fichier |
| If you enable this option, the pattern will be treated as a regular expression and matched using the Perl-compatible regular expressions (PCRE). Check the documentation for details about the regular expression syntax. | Se activatz aquesta opcion, lo tèxte serà tractat coma una expression regulara amb una aisina compatibla Perl (PCRE). Consultatz la documentacion per mai de detalhs sus la sintaxi de las expressions regularas. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | avec \| comme \| outil \| plus \| une |
| If you frequently create certain kinds  of documents, make a copy of one and put it in this folder. Thunar will add an entry for this document in the "Create Document" menu.<br><br>You can then select the entry from the "Create Document" menu and a copy of the document will be created in the directory you are viewing. | Se creatz frequentament un certan tipe<br>de document, fasètz-ne una còpia dins aqueste dorsièr. Thunar apondrà una entrada per aqueste document dins lo menú « Crear un document ».<br><br>Podètz seleccionar aquesta entrada dins lo menú « Crear un document » e una còpia d'aqueste document serà creada dins lo dorsièr en cors. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | dans \| dossier \| une |
| If you select this option your choice will be remembered and you won't be asked again. You can use the preferences dialog to alter your choice afterwards. | Se seleccionatz aquesta opcion, vòstra causida serà memorizada e la question vos serà pas mai pausada. Podètz utilizar la bóstia de dialòg de las preferéncias per modificar vòstra causida ulteriorament. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | plus |
| Image Files | Fichièrs imatge | Fichèrs imatge | fichier |
| Include additional files in the list of files to be renamed | Inclure de fichièrs addicionals dins la lista de fichièrs de renomenar | Inclure de fichèrs addicionals dens la lista de fichèrs de renomenar | dans \| fichier |
| Insert Date / Time | Inserir la data / l'ora | Inserir la data / l'òra | heure |
| Invalid desktop file | Fichièr de burèu invalid | Fichèr de burèu invalid | fichier |
| Invalid filename "%s" | Nom de fichièr invalid « %s » | Nom de fichèr invalid « %s » | fichier |
| Invalid filename provided by XDS drag site | Nom de fichièr invalid provesit pel lisat del site XDS | Conservé : Sens, accord ou terminologie technique de la source non validés. | du \| fichier |
| Invalid regular expression, at character position %ld: %s | Expression regulara invalida, a la posicion del caractèr %ld : %s | Expression regulara invalida, a la posicion deu caractèr %ld : %s | du |
| Keyboard _Shortcut: | Acorchis de _clavièr : | Acorchis de _clavèr : | clavier |
| Keyboard shortcut already in use | Acorchis de clavièr ja utilizat | Acorchis de clavèr dejà utilizat | clavier \| deja |
| Last Active View | Darrièra vista activa | Darrèra vista activa | derniere |
| Last Modified | Darrièra modificacion | Darrèra modificacion | derniere |
| Last Modified: %s | Darrièra modificacion : %s | Darrèra modificacion : %s | derniere |
| Link Target: | Cibla del ligam : | Cibla deu ligam : | du |
| Loading folder contents... | Cargament del contengut del dorsièr... | Cargament deu contiengut deu dossièr... | contenu \| dossier \| du |
| Local Files Only | Fichièrs locals solament | Fichèrs locals solament | fichier |
| Mixed file owners | Proprietari del fichièr mixte | Conservé : Sens, accord ou terminologie technique de la source non validés. | du \| fichier |
| Mo_ve to Trash | Desplaçar  dins l'escobilhièr | Desplaçar dens l'_escobilhièr | deplacer \| dans |
| Modern approach with buttons that correspond to folders | Apròchi modèrne amb los botons que correspondon als dorsièrs | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | aux \| avec \| dossier |
| Mount and open %s (%s) | Montar e dobrir %s (%s) | Montar e obrir %s (%s) | ouvrir |
| Move or copy files previously selected by a Cut or Copy command | Desplaçar o copiar de fichièrs prealablament seleccionats per una comanda Talhar o Copiar | Desplaçar o copiar de fichèrs prealablament seleccionats per ua comanda Talhar o Copiar | fichier \| une |
| Move or copy files previously selected by a Cut or Copy command into the selected folder | Desplaçar o copiar de fichièrs prealablament seleccionats per una comanda Talhar o Copiar dins lo dorsièr seleccionat | Desplaçar o copiar de fichèrs prealablament seleccionats per ua comanda Talhar o Copiar dens lo dossièr seleccionat | dans \| dossier \| fichier \| une |
| Move the currently selected action down by one row. | Davalar d'una linha l'accion actualament seleccionada. | Davalar d'ua linha l'accion actualament seleccionada. | une |
| Move the currently selected action up by one row. | Montar d'una linha l'accion actualament seleccionada. | Montar d'ua linha l'accion actualament seleccionada. | une |
| Moving files ... | Desplaçament des fichièrs... | Desplaçament deus fichèrs... | des \| fichier |
| Moving files into "%s"... | Desplaçament dels fichièrs dins « %s » ... | Desplaçament deus fichèrs dens « %s » ... | dans \| des \| fichier |
| Moving files into the trash... | Desplaçament dels fichièrs dins l'escobilhièr... | Desplaçament deus fichèrs dens l'escobilhièr... | dans \| des \| fichier |
| Name '%s' lost on the message dbus. | Nom « %s » perdut sul dbus de messatge. | Nom « %s » perdut suu dbus de messatge. | sur_le |
| Never | Pas jamai | Pas jamèi | jamais |
| New Empty File | Novèl fichièr void | Navèth fichèr vueit | fichier \| nouveau \| vide |
| New Empty File... | Novèl fichièr void... | Navèth fichèr vueit... | fichier \| nouveau \| vide |
| New File | Fichièr novèl | Fichèr navèth | fichier \| nouveau |
| New Folder | Dorsièr novèl | Dossièr navèth | dossier \| nouveau |
| New Name | Nom novèl | Nom navèth | nouveau |
| New _Tab | Ongle_t novèl | Ongle_t navèth | nouveau |
| New _Window | Fenèstra _novèla | Frinèsta _navèra | fenetre \| nouvelle |
| No renamer modules were found on your system. Please check your<br>installation or contact your system administrator. If you install Thunar<br>from source, be sure to enable the "Simple Builtin Renamers" plugin. | Cap de modul per renomenar es pas estat trobat sus vòstre sistèma.<br>Se vos plai, verificatz vòstra installacion o contactatz vòstre administrator del sistèma. Se installatz Thunar a partir de las fonts, asseguratz-vos d'activar l'empeuton « Simple Builtin Renamers ». | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | du |
| No templates installed in<br>"%s" | Cap de modèl pas installat dins<br> « %s » | Cap de modèle pas installat dens<br> « %s » | dans \| modele |
| Normal Si_ze | Talha _normala | Talha _normau | normal |
| Only show thumbnails for files smaller than: | Far veire las miniaturas sonque pels fichièrs inferiors a : | Har véder las miniaturas sonque entaus fichèrs inferiors a : | faire \| fichier \| pour_les \| voir |
| Open | Dobrir | Obrir | ouvrir |
| Open <i>%s</i> and other files of type "%s" with: | Dobrir <i>%s</i>  e autres fichièrs de tipe « %s » amb : | Obrir <i>%s</i>  e autes fichèrs de tipe « %s » dab : | autres \| avec \| fichier \| ouvrir |
| Open Item Location | Dobrir l'emplaçament de l'element | Obrir l'emplaçament de l'element | ouvrir |
| Open Terminal Here | Dobrir un terminal aicí | Obrir un terminal ací | ici \| ouvrir |
| Open With | Dobrir amb | Obrir dab | avec \| ouvrir |
| Open With Other _Application... | Dobrir amb una autra _aplicacion... | Obrir dab ua auta _aplicacion... | autre \| avec \| ouvrir \| une |
| Open _Parent | Dobrir lo dorsièr _parent | Obrir lo dossièr _parent | dossier \| ouvrir |
| Open a new Thunar window for the displayed location | Dobrir una fenèstra novèla Thunar per l'endrech afichat | Obrir ua frinèsta navèra Thunar per l'endrech afichat | fenetre \| nouvelle \| ouvrir \| une |
| Open a new tab for the displayed location | Dobrir una onglet novèl per l'endrech afichat | Obrir un onglet navèth entà l'endrech afichat | ouvrir \| nouveau \| pour |
| Open current folder in a new window | Dobrir lo repertòri corrent dins una fenèstra novèla | Obrir lo dossièr corrent dens ua frinèsta navèra | dans \| dossier \| fenetre \| nouvelle \| ouvrir \| une |
| Open folders | Dobrir los dorsièrs | Obrir los dossièrs | dossier \| ouvrir |
| Open folders in new tabs on middle click | Dobrir los dorsièrs dins un onglet novèl amb lo clic de la rodeta de la mirga | Obrir los dossièrs dens un onglet navèth dab lo clic de la rodeta de la soritz | avec \| dans \| dossier \| nouveau \| ouvrir \| souris |
| Open in new _Tab | Dobrir dins un _onglet novèl | Obrir dens un _onglet navèth | dans \| nouveau \| ouvrir |
| Open in new _Window | Dobrir dins una _fenèstra novèla | Obrir dens ua _frinèsta navèra | dans \| fenetre \| nouvelle \| ouvrir \| une |
| Open the bulk rename dialog | Dobrir la bóstia de dialòg de cambiament de nom en massa | Obrir la bóstia de dialòg de cambiament de nom en massa | ouvrir |
| Open the desktop folder | Dobrir lo repertòri del burèu | Obrir lo dossièr deu burèu | dossier \| du \| ouvrir |
| Open the home folder | Dobrir lo repertòri personal | Obrir lo dossièr personau | dossier \| ouvrir \| personnel |
| Open the parent folder | Dobrir lo dorsièr parent | Obrir lo dossièr parent | dossier \| ouvrir |
| Other Application... | Autra aplicacion... | Auta aplicacion... | autre |
| Other Applications | Autras aplicacions | Autas aplicacions | autre |
| Others | Autres | Autes | autres |
| PDA | Assistent personal | Assistent personau | personnel |
| Paste the clipboard | Pega lo contengut del quichapapièrs | Pegar lo contiengut deu quichapapièrs | coller \| contenu \| du |
| Prepare the selected files to be copied with a Paste command | Preparar los fichièrs seleccionats a èsser copiats per una comanda Pegar | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | fichier \| une |
| Prepare the selected files to be moved with a Paste command | Prepara los fichièrs seleccionats a èsser desplaçats per la comanda Pegar | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | fichier |
| Quit a running Thunar instance | Quitar una instància de Thunar en cors d'execucion | Quitar ua instància de Thunar en cors d'execucion | une |
| Reload the current folder | Recargar lo dorsièr corrent | Recargar lo dossièr corrent | dossier |
| Remove all files and folders from the Trash? | Suprimir totes los fichièrs e dorsièrs de l'escobilhièr ? | Suprimir tots los fichèrs e dossièrs de l'escobilhièr ? | supprimer \| tous \| fichier \| dossier |
| Remove the selected files from Recent | Suprimir los fichièrs seleccionats de la lista dels Recents | Suprimir los fichèrs seleccionats de la lista deus Recents | des \| fichier |
| Rena_me All | Reno_menar totes | Reno_menar tots | tous |
| Rename Multiple Files | Renomenar mantun fichièr | Renomenar mantun fichèr | fichier |
| Restoring files... | Restabliment dels fichièrs... | Restabliment deus fichèrs... | des \| fichier |
| Run in _terminal | Executar dins un _terminal | Executar dens un _terminal | dans |
| Search | Recercar | Cercar | chercher |
| Select _all Files | Seleccionar _totes los fichièrs | Seleccionar _tots los fichèrs | fichier \| tous |
| Select all files but not those currently selected | Seleccionar totes los elements que son pas seleccionats | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | tous |
| Select all files in this window | Seleccionar totes los fichièrs dins aquesta fenèstra | Seleccionar tots los fichèrs de la frinèsta | selectionner \| tous \| fichier \| fenetre |
| Select all files that match a certain pattern | Seleccionar totes los fichièrs que correspondon a un certan motiu | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | fichier \| tous |
| Select an Application | Causissètz una Aplicacion | Causir ua aplicacion | choisir \| une \| application |
| Select an Icon for "%s" | Seleccionar una icòna per « %s » | Seleccionar ua icòna per « %s » | une |
| Select files to rename | Seleccionar los fichièrs de renomenar | Seleccionar los fichèrs de renomenar | fichier |
| Select this option to display icon emblems in the shortcuts pane for all folders for which emblems have been defined in the folders properties dialog. | Seleccionatz aquesta opcion per afichar d'icònas dels emblèmas dins lo panèl dels acorchis per totes los dorsièrs pels quals d'emblèmas son estats definits dins las proprietats. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | dans \| des \| dossier \| panneau \| tous |
| Select this option to display icon emblems in the tree pane for all folders for which emblems have been defined in the folders properties dialog. | Seleccionatz aquesta opcion per afichar los emblèmas dins l'arborescéncia per totes los dorsièrs pels quals d'emblèmas son estats definits dins las proprietats. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | dans \| dossier \| tous |
| Select this option to enable startup notification when the command is run from the file manager or the menu. Not every application supports startup notification. | Seleccionatz aquesta opcion per activar la notificacion d'aviada quand la comanda es executada a partir del gestionari de fichièrs o lo menú. Totas las aplicacions supòrtan pas la notificacion d'aviada. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | du \| fichier |
| Select this option to list folders before files when you sort a folder. | Seleccionatz aquesta opcion per far la lista dels dorsièrs abans los fichièrs quand triatz un dorsièr. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | des \| dossier \| faire \| fichier |
| Select this option to place the icon captions for items beside the icon rather than below the icon. | Seleccionatz aquesta opcion per plaçar la legenda dels elements al costat de l'icòna al luòc d'en dejós. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | au \| des \| dessous |
| Select this option to restore your tabs as they were last time you used Thunar | Seleccionatz aquesta opcion per restaurar los onglets coma èran lo darrièr còp qu’utilizaretz Thunar | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | comme \| derriere |
| Select this option to run the command in a terminal window. | Seleccionatz aquesta opcion per executar la comanda dins una fenèstra de terminal. | Seleccionar aquera opcion entà executar la comanda dens ua frinèsta de terminal. | selectionner \| option \| pour \| executer \| dans \| une \| fenetre |
| Select this option to show file size in binary format instead of decimal. | Seleccionar aquesta opcion per afichar la talha dels fichièrs al format binari puslèu que decimal. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | au \| des \| fichier |
| Send "%s" as compressed archive? | Mandar « %s » en tant qu'archiu compressat ? | Enviar « %s » en tant qu'archiu compressat ? | envoyer |
| Send _directly | Mandar _dirèctament | Enviar _dirèctament | envoyer |
| Send as _archive | Mandar en tant qu'_archiu | Enviar en tant qu'_archiu | envoyer |
| Send com_pressed | Mandar com_pressat | Enviar com_pressat | envoyer |
| Send to _Desktop | Enviar al _burèu | Enviar au _burèu | au |
| Set _Foreground | Definir _primièr plan | Definir _purmèr plan | premier |
| Set as wallpaper | Definir coma fons d'ecran | Definir com hons d'ecran | comme \| fond |
| Set this file as trusted | Definir aqueste fichièr coma fisable | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | comme \| fichier |
| Setup custom actions that will appear in the file managers context menus | Configurar las accions personalizadas qu'apareisseràn dins los menús contextuals del gestionari de fichièrs | Configurar las accions personalizadas qu'apareisseràn dens los menús contextuals deu gestionari de fichèrs | dans \| du \| fichier |
| Shortcuts Pane | Panèl dels acorchis | Panèu deus acorchis | des \| panneau |
| Show Icon _Emblems | Afichar l’icòna dels _emblèmas | Afichar l’icòna deus _emblèmas | des |
| Show _Hidden Files | Far veire los fichièrs a_magats | Har véder los fichèrs a_magats | faire \| fichier \| voir |
| Show action to permanently delete files and folders | Afichar la foncion per suprimir definitivament los fichièrs e dorsièrs | Afichar la foncion per suprimir definitivament los fichèrs e dossièrs | dossier \| fichier |
| Show file size in binary format | Afichar la talha dels fichièrs al format binari. | Afichar la talha deus fichèrs au format binari. | au \| des \| fichier |
| Show filetype | Afichar lo tipe de fichièr | Afichar lo tipe de fichèr | fichier |
| Show last modified | Afichar las darrièras modificacions | Afichar las darrèras modificacions | derniere |
| Show the contents at the normal size | Afichar lo contengut amb una talha normala | Afichar lo contiengut dab ua talha normau | afficher \| contenu \| avec \| une \| taille \| normal |
| Show the contents in less detail | Afichar lo contengut amb mens de detalhs | Afichar lo contiengut dab mensh de detalhs | avec \| contenu \| moins |
| Show the contents in more detail | Afichar lo contengut amb mai de detalhs | Afichar lo contiengut dab mei de detalhs | avec \| contenu \| plus |
| Show thumbnails: | Far veire las miniaturas : | Har véder las miniaturas : | faire \| voir |
| Side Pane | Panèl lateral | Panèu lateral | panneau |
| Software: | Logicials : | Logiciaus : | logiciel |
| Sort _folders before files | Triar los _dorsièrs abans los fichièrs | Triar los _dossièrs abans los fichèrs | dossier \| fichier |
| Sort items in ascending order | Triar los elements per òrdre creissent | Triar los elements per òrdi creissent | ordre |
| Sort items in descending order | Triar los elements per òrdre descreissent | Triar los elements per òrdi descreissent | ordre |
| Specify a location to open | Especificar un emplaçament de dobrir | Especificar un emplaçament d'obrir | ouvrir |
| Specify the d_elay before an item gets selected<br>when the mouse pointer is paused over it: | Especificatz lo re_lambi abans qu'un element siá<br>seleccionat quand lo puntador de la mirga se<br>plaça dessús : | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | souris |
| Starting... (User request) | Lançament... (Utilizaire interrogat) | Conservé : Sens, accord ou terminologie technique de la source non validés. | utilisateur |
| T_emplates | Modè_ls | Modè_les | modele |
| Text _Format: | _Format del tèxte : | _Format deu tèxte : | du |
| The Thunar development team. All rights reserved. | L'equipa de desvolopament de Thunar. Totes los dreches reservats. | L'equipa de desvolopament de Thunar. Tots los dreches reservats. | tous |
| The URL to the documentation of the renamer | L'URL de la documentacion del renomenador | L'URL de la documentacion deu renomenador | du |
| The command (including the necessary parameters) to perform the action. See the command parameter legend below for a list of supported parameter variables, which will be substituted when launching the command. When upper-case letters (e.g. %F, %D, %N) are used, the action will be applicable even if more than one item is selected. Else the action will only be applicable if exactly one item is selected. | La comanda (qu'inclutz los paramètres necessaris) per executar aquesta accion. Veire la legenda dels paramètres de comanda per una lista de las variablas suportadas, que seràn remplaçadas a l'aviada de la comanda. Quand una letra majuscula (i.e. %F, %D, %N) es utilizada, l'accion es aplicabla quitament se mai d'un element es seleccionat. Siquenon l'accion es unicament aplicabla a l'element seleccionat. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | des \| plus \| une \| voir |
| The description of the action that will be displayed as tooltip in the statusbar when selecting the item from the context menu. | La descripcion de l'accion qu'apareisserà coma astúcia dins la barra d'estatut quand l'element es seleccionat a partir del menú contextual. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | comme \| dans \| du |
| The desktop file "%s" is in an insecure location and not marked as executable. If you do not trust this program, click Cancel. | Lo fichièr de burèu « %s » es dins una situacion pas securizada e pas marcat coma executables. Se vos fisatz pas d'aqueste programa, clicatz sus Anullar. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | comme \| dans \| fichier \| une |
| The device "%s" is being unmounted by the system. Please do not remove the media or disconnect the drive | Lo periferic « %s » es en cors de desmontatge pel sistèma. Levetz pas lo supòrt o desconnectetz pas lo lector. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | par_le |
| The directory "%s" does not exist. Do you want to create it? | Lo repertòri « %s » existís pas. Lo volètz crear ? | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | dossier |
| The file "%s" already exists | Lo fichièr « %s » existís ja | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | deja \| fichier |
| The file "%s" already exists. Would you like to replace it?<br><br>If you replace an existing file, its contents will be overwritten. | Lo fichièr « %s » existís ja. Lo volètz remplaçar ?<br><br>Se remplaçatz un fichièr existent, son contengut serà espotit. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | contenu \| deja \| fichier |
| The folder "%s" does not exist anymore but is required to restore the file "%s" from the trash | Lo dorsièr « %s » existís pas mai, mas es necessari per restablir lo fichièr « %s » de l'escobilhièr | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | dossier \| fichier \| plus |
| The folder permissions will be reset to a consistent state. Only users allowed to read the contents of this folder will be allowed to enter the folder afterwards. | Los dreches del dorsièr seràn remeses dins un estat coerent. Sols los utilizaires autorizats a legir lo contengut d'aqueste dorsièr seràn autorizats a i entrar. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | contenu \| dans \| dossier \| du \| lire \| utilisateur |
| The format describes the date and time parts to insert into the file name. For example, %Y will be substituted with the year, %m with the month and %d with the day. See the documentation of the date utility for additional information. | Lo format descriu las partidas de la data e l'ora d'inserir dins lo nom del fichièr. Per exemple, %Y serà substituit per l'annada, %m pel mes, e %d pel jorn. Consultatz d'informacions suplementàrias a prepaus de las datas dins la documentacion. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | dans \| du \| fichier \| heure \| jour \| par_le |
| The generic name of the entry, for example "Web Browser" in case of Firefox. | Lo nom generic de l'entrada, per exemple « Navigador Web » dins lo cas de Firefox. | Lo nom generic de l'entrada, per exemple « Navigador Web » dens lo cas de Firefox. | dans |
| The icon size for the path entry | La talha de l'icòna pel camin d'accès | La talha de l'icòna entau camin d'accès | pour_le |
| The keyboard shortcut for the action. | L’acorchi de clavièr per l'action. | L’acorchi de clavèr per l'action. | clavier |
| The name of the action that will be displayed in the context menu. | Lo nom de l'accion qu'apareisserà dins lo menú contextual. | Lo nom de l'accion qu'apareisserà dens lo menú contextual. | dans |
| The number of source and target filenames must be the same | Lo nombre de fichièrs font e destinatari devon èsser los meteisses | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | fichier \| source |
| The path "%s" does not refer to a directory | Lo camin « %s » fa pas referéncia a un repertòri | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | dossier |
| The program to execute, possibly with arguments. | Lo programa d'executar, amb sos arguments eventuals. | Lo programa d'executar, dab sos arguments eventuals. | avec |
| The root folder has no parent | Lo dorsièr raiç a pas de parent | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | dossier |
| The selected application is used to open this and other files of type "%s". | L'aplicacion seleccionada es utilizada per dobrir aquò e d'autres fichièrs de tipe « %s ». | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | autres \| fichier \| ouvrir |
| The user visible name of the renamer | Lo nom d'utilizaire visible del renomenador | Lo nom d'utilizator visible deu renomenador | du \| utilisateur |
| The working directory for the program. | Lo repertòri de trabalh pel programa. | Lo dossièr de tribalh entau programa. | dossier \| pour_le \| travail |
| The working directory must be an absolute path | Lo repertòri de trabalh deu èsser un camin absolut | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | dossier \| travail |
| There is data that needs to be written to the device "%s" before it can be removed. Please do not remove the media or disconnect the drive | De donadas devon èsser escrichas sul periferic « %s » abans sa desconnexion. Levetz pas lo supòrt o desconnectetz pas lo lector. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | donnees \| sur_le |
| There is not enough space on the destination. Try to remove files to make space. | I a pas pro d'espaci dins la destinacion. Ensajatz de suprimir de fichièrs per liberar d'espaci. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | dans \| fichier |
| There is nothing on the clipboard to paste | I a pas res a pegar dins lo quichapapièrs | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | dans |
| This folder already contains a file "%s". | Aqueste dorsièr conten ja un fichièr « %s ». | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | deja \| dossier \| fichier |
| This folder already contains a folder "%s". | Aqueste dorsièr conten ja un dorsièr « %s ». | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | deja \| dossier |
| This folder already contains a symbolic link "%s". | Aqueste dorsièr conten ja un ligam simbolic « %s ». | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | deja \| dossier |
| This keyboard shortcut is currently used by: '%s' | L'acorchi de clavièr es ja utilizat per : « %s » | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | clavier \| deja |
| This will dissociate the application launcher for this file type, but will not uninstall or remove the application launcher itself. | Aquò desassociarà l’aviador d’aplicacion d’aqueste tipe de fichièr, mas desinstallarà o suprimirà pas lo quite aviador. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | fichier |
| This will remove the application launcher that appears in the file context menu, but will not uninstall the application itself.<br><br>You can only remove application launchers that were created using the custom command box in the "Open With" dialog of the file manager. | Aquò permetrà de suprimir l'aviador d'aplicacion que s'aficha dins lo menú contextual del fichièr, mas desinstallarà pas l'aplicacion ela-meteissa.<br><br>Podètz solament suprimir los aviadors d'aplicacions creats amb l'ajuda de la bóstia de comanda personalizada dins la bóstia de dialòg « Dobrir amb »  del gestionari de fichièrs. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | avec \| dans \| du \| fichier \| ouvrir |
| Thunar Bulk Rename is a powerful and extensible<br>tool to rename multiple files at once. | L'aisina Thunar « Renomenar en massa » es poderós e extensible per renomenar mantun fichièr a l'encòp ! | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | fichier \| outil |
| Thunar File Manager | Gestionari de Fichièrs Thunar | Gestionari de Fichèrs Thunar | fichier |
| Thunar is a fast and easy to use file manager<br>for the Xfce Desktop Environment. | Thunar es un gestionari de fichièrs rapid e aisit<br>d'utilizacion per l'environament de burèu Xfce. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | fichier \| rapide |
| Thunar is a file browser specifically designed for the Xfce Desktop, but also can serve as an alternate file browser for other Desktop environments. It has a simple, clean two-pane design for browsing all your files. | Thunar es un gestionari de fichièrs concebut especificament pel burèu Xfce, mas pòt tanben servir coma gestionari de fichièrs alternatiu per d’autres environaments de burèu. Dispausa d’una interfàcia de dos panèls simpla e epurada per percórrer totes vòstres fichièrs. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | autres \| comme \| fichier \| panneau \| pour_le \| tous \| une |
| Today | Uèi | Uei | aujourdhui |
| Today / Custom | Uèi / Personalizat | Uei / Personalizat | aujourdhui |
| Today at %X | Uèi a %X | Uei a %X | aujourdhui |
| Toggles the display of hidden files in the current window | Far veire/amagar los fichièrs amagats dins la fenèstra correnta | Har véder/amagar los fichèrs amagats dens la frinèsta correnta | dans \| faire \| fenetre \| fichier \| voir |
| Toggles the visibility of the shortcuts pane | Cambiar la visibilitat del panèl dels acorchis | Cambiar la visibilitat deu panèu deus acorchis | des \| du \| panneau |
| Toggles the visibility of the tree pane | Cambiar la visibilitat del panèl d'arborescéncia | Cambiar la visibilitat deu panèu d'arborescéncia | du \| panneau |
| Tooltip for the entry, for example "View sites on the Internet" in case of Firefox. Should not be redundant with the name or the description. | La bulla d'ajuda de l'entrda, per exemple « Visualizar los sites sus Internet » dins lo cas de Firefox. Lo tèxte deu evitar de repetir lo nom o la descripcion. | La bulla d'ajuda de l'entrda, per exemple « Visualizar los sites sus Internet » dens lo cas de Firefox. Lo tèxte deu evitar de repetir lo nom o la descripcion. | dans |
| Transfer files in parallel: | Transferir los fichièrs en parallèl : | Transferir los fichèrs en parallèl : | fichier |
| Trash contains files | L'escobilhièr conten de fichièrs | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | fichier |
| Trash is empty | Escobilhièr void | Escobilhièr vueit | vide |
| Tree Pane | Panèl d'arborescéncia | Panèu d'arborescéncia | panneau |
| U_nselect all Files | _Deseleccionar totes los fichièrs | _Deseleccionar tots los fichèrs | fichier \| tous |
| Undo the latest operation | Desfar la darrièra operacion | Desfar la darrèra operacion | derniere |
| Unknown | Desconegut | Desconeishut | inconnu |
| Unknown closing element <%s> | Element de tampadura <%s> desconegut | Element de tampadura <%s> desconeishut | inconnu |
| Unknown file owner | Proprietari del fichièr desconegut | Proprietari deu fichèr desconeishut | du \| fichier \| inconnu |
| Unknown user "%s" | Utilizaire desconegut « %s » | Utilizator desconeishut « %s » | inconnu \| utilisateur |
| Unmounting device | Desmontatge del periferic | Desmontatge deu periferic | du |
| Unselect all files in this window | Deseleccionar totes los fichièrs d’aquesta fenèstra | Deseleccionar tots los fichèrs de la frinèsta | tous \| fichier \| fenetre |
| Untitled document | Document sens nom | Document shens nom | sans |
| Use a _custom command: | Utilizar una _comanda personalizada : | Utilizar ua _comanda personalizada : | une |
| Use a custom command for an application that is not available from the above application list. | Utilizar una comanda personalizada per una aplicacion absenta de la lista çaisús | Utilizar ua comanda personalizada per ua aplicacion absenta de la lista çaisús | une |
| Use as _default for this kind of file | Utilizar aquesta accion per _defaut per aqueste tipe de fichièr | Utilizar per _defaut entà aqueth tipe de fichèr | utiliser \| pour \| type \| fichier |
| Use current folder icon | Utilizar l’icòna de dorsièr actuala | Utilizar l’icòna de dossièr actuau | actuel \| dossier |
| Video Files | Fichièrs vidèo | Fichèrs video | fichier \| video |
| View _new folders using: | Veire un _novèl dorsièr en utilizant : | Véder un _navèth dossièr en utilizant : | dossier \| nouveau \| voir |
| View the properties of the selected file | Aficha las proprietats del fichièr seleccionat | Afichar las proprietats deu fichèr seleccionat | afficher \| proprietes \| du \| fichier |
| When changing the permissions of a folder, you<br>can also apply the changes to the contents of the<br>folder. Select the default behavior below: | Quand cambiatz las permissions d'un dorsièr,<br>podètz aplicar aquestes cambiaments al contengut<br>d'aqueste. Seleccionatz lo comportament per defaut : | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | au \| contenu \| dossier |
| When sending a file via email, you can either choose to send the file directly, as is, or compress the file before attaching it to an email. It is highly recommended to compress large files before sending them. | Al moment del mandadís d'un fichièr per corrièr electronic, podètz causir de mandar dirèctament lo fichièr, tal coma es, o compressar lo fichièr abans de l'estacar a un corrièr electronic. Es fòrtament recomandat de compressar de fichièrs voluminoses abans de los mandar. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | au \| comme \| du \| envoyer \| fichier |
| When sending multiple files via email, you can either choose to send the files directly, attaching multiple files to an email, or send all files compressed into a single archive file and attach the archive. It is highly recommended to send multiple large files as archive. | Al moment de mandadisses de fichièrs per corrièr electronic, avètz la causida entre los mandar dirèctament en los jonhent totes al corrièr electronic o jos la forma compressada dins un archiu en estacant aquesta darrièra al corrièr electronic. Es fòrtament conselhat de compressar los fichièrs d'una certana talha. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | au \| dans \| derniere \| envoyer \| fichier \| tous \| une |
| When single-click activation is enabled, pausing the mouse pointer over an item will automatically select that item after the chosen delay. You can disable this behavior by moving the slider to the left-most position. This behavior may be useful when single clicks activate items, and you want only to select the item without activating it. | Quand l'activacion per un clic simple es activat, lo fach d'arrestar lo puntador de la mirga sus un element lo seleccionarà automaticament aprèp lo relambi causit. Aqueste comportament pòt èsser desactivat en desplaçant lo cursor cap a la posicion esquèrra absoluda. Aquò pòt èsser utile quand un clic simple activa los elements e que volètz solament seleccionar aqueles sens los activar. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | sans \| souris |
| Window | Fenèstra | Frinèsta | fenetre |
| Window Icon | Icòna fenèstra | Icòna frinèsta | fenetre |
| Working Directory: | Repertòri de trabalh : | Dossièr de tribalh : | dossier \| travail |
| Writing data to device | Escritura de las donadas sul periferic | Escritura de las dadas suu periferic | donnees \| sur_le |
| Yesterday | Ièr | Ger | hier |
| Yesterday at %X | Ièr a %X | Ger a %X | hier |
| You can either choose to skip this file and continue to rename the remaining files, or revert the previously renamed files to their previous names, or cancel the operation without reverting previous changes. | Podètz causir siá d'ignorar aqueste fichièr e contunhar de renomenar los fichièrs restants, siá d'anullar los cambiament de noms efectuats suls fichièrs precedents, siá d'interrompre l'operacion sens anullar las modificacions aportadas. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | fichier \| sans \| sur_les |
| ZIP command terminated with error %d | La comanda ZIP s'es acabada amb l'error %d | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | avec |
| _Add Bookmark | _Apondre als marcapaginas | _Ajustar aus marcapaginas | ajouter \| aux |
| _Add Files... | _Apondre de fichièrs... | _Ajustar de fichèrs... | ajouter \| fichier |
| _Audio Files | Fichièrs _àudio | Fichèrs _àudio | fichier |
| _Close | _Tampar | _Barrar | fermer |
| _Close Window | Tampar la fenèstra | _Barrar la frinèsta | fermer \| fenetre |
| _Copy here | _Copiar aicí | _Copiar ací | ici |
| _Edit Launcher | _Editar l'aviador | _Modificar l'aviador | modifier |
| _Empty File | _Fichièr void | _Fichèr vueit | fichier \| vide |
| _Empty Trash | _Voidar l'escobilhièr | _Vueitar l'escobilhièr | vider |
| _File | _Fichièr | _Fichèr | fichier |
| _File Pattern: | _Motiu dels fichièrs : | _Motiu deus fichèrs : | des \| fichier |
| _Home | _Dorsièr personal | _Dossièr personau | dossier \| personnel |
| _Image Files | Fichièrs _imatge | Fichèrs _imatge | fichier |
| _Link here | _Ligar aicí | _Ligar ací | ici |
| _Lock | _Verrolhar | _Varrolhar | verrouiller |
| _Move here | _Desplaçar aicí | _Desplaçar ací | ici |
| _Number Format: | Format dels _nombres : | Format deus _nombres : | des |
| _OK | _D'acòrdi | _D'acòrd | accord |
| _Open | _Dobrir | _Obrir | ouvrir |
| _Open Location... | _Dobrir l'emplaçament ... | _Obrir l'emplaçament ... | ouvrir |
| _Open With "%s" | _Dobrir amb « %s » | _Obrir dab « %s » | avec \| ouvrir |
| _Open With Default Applications | _Dobrir amb las aplicacions per defaut | _Obrir dab las aplicacions per defaut | avec \| ouvrir |
| _Open With: | _Dobrir amb : | _Obrir dab : | avec \| ouvrir |
| _Other Files | Autres _fichièrs | Autes _fichèrs | autres \| fichier |
| _Paste Into Folder | _Pegar dins lo dorsièr | _Pegar dens lo dossièr | dans \| dossier |
| _Remember view settings for each folder | _Memorizar los reglatges d’afichatge per cada dorsièr | _Memorizar los reglatges d’afichatge per cada dossièr | dossier |
| _Remove from Recent | _Suprimir dels recents | _Suprimir deus recents | des |
| _Reset | _Reïnicializar | _Tornar inicializar | reinitialiser |
| _Restore and Show | _Restaurar e veire | _Restaurar e véder | voir |
| _Restore and show the file(s) | _Restaurar e veire lo(s) fichièr(s) | _Restaurar e véder lo(s) fichèr(s) | fichier \| voir |
| _Search for Files... | _Recercar de fichièrs... | _Cercar de fichèrs... | chercher \| fichier |
| _Send To | _Mandar cap a | _Enviar cap a | envoyer |
| _Side Pane | _Panèl lateral | _Panèu lateral | panneau |
| _Skip This File | _Ignorar aqueste fichièr | _Ignorar lo fichèr | fichier |
| _Text Files | Fichièrs _tèxte | Fichèrs _tèxte | fichier |
| _Text beside icons | _Tèxte al costat de las icònas | _Tèxte au costat de las icònas | au |
| _Video Files | Fichièrs _vidèo | Fichèrs _video | fichier \| video |
| bulk;renamer;renaming;thunar;files;folders;directory;directories; | massa;grop;renomenar;renomatge;thunar;fichièrs;dorsièrs;dossièrs;repertòris; | massa;grop;renomenar;renomatge;thunar;fichèrs;dossièrs;dossièrs;dossièrs; | dossier \| fichier |
| directories containing the files that are passed in %F | repertòris que conten los fichièrs que son passats dins %F | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | dans \| dossier \| fichier |
| directory containing the file that is passed in %f | repertòri que conten lo fichièr qu'es passat dins %f | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | dans \| dossier \| fichier |
| file manager;explorer;finder;browser;folders;directory;directories;partitions;drives;network;devices;rename;move;copy;delete;permissions;home;trash; | gestionari de fichièrs;explorar;navigar;navegar;dossièrs;dorsièrs;repertòris;particions;lectors;ret;malhum;periferics;aparelhs;renomenar;renommar;desplaçar;suprimir;permissions;autorizacions;personal;escobilhièr;banasta;desca;desqueta;guirba;bordilhièr;pobèlla; | Conservé : Contexte technique ou long : relecture intégrale nécessaire. | dossier \| fichier \| personnel |
| the first selected filename (without path) | lo primièr nom de fichièr seleccionat (sens lo camin) | lo purmèr nom de fichèr seleccionat (shens lo camin) | fichier \| premier \| sans |
| the selected filenames (without paths) | los noms dels fichièrs seleccionats (sens los camins) | los noms deus fichèrs seleccionats (shens los camins) | des \| fichier \| sans |
| thunar;settings;preferences;configure;thumbnails;file size;date format;shortcuts pane;tree view;tabs; | thunar;paramètres;reglatges;preferéncias;configurar;vinhetas;miniaturas;talha de fichièr;format de data;acorchi;panèl;arbre;onglets; | thunar;paramètres;reglatges;preferéncias;configurar;vinhetas;miniaturas;talha de fichèr;format de data;acorchi;panèu;arbre;onglets; | fichier \| panneau |
| unknown | Desconegut | Desconeishut | inconnu |
| with the following file? | per lo fichièr seguent ? | dab lo fichèr seguent ? | avec \| fichier \| suivant |
| with the following folder? | per lo dorsièr seguent ? | dab lo dossièr seguent ? | avec \| dossier \| suivant |

## xfwm4

| Clé source | Occitan livré | Béarnais retenu ou motif de conservation | Glossaire |
|---|---|---|---|
| %s: %s<br>Try %s --help to see a full list of available command line options.<br> | %s : %s<br>Ensajatz %s --help per afichar una lista completa de las opcions de linha de comanda.<br> | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | une |
| <b>Button layout</b> | <b>Agençament dels botons</b> | <b>Agençament deus botons</b> | des |
| <b>Double click _action</b> | <b>_Accion del clic doble</b> | <b>_Accion deu clic doble</b> | du |
| <b>Focus model</b> | <b>Modèl de focalizacion</b> | <b>Modèle de focalizacion</b> | modele |
| <b>Hide content of windows</b> | <b>Amagar lo contengut de las fenèstras</b> | Conservé : Flexion nouvelle non attestée dans les sources consultées. | contenu |
| <b>New window focus</b> | <b>Focalizar las novèlas fenèstras</b> | Conservé : Flexion nouvelle non attestée dans les sources consultées. | nouvelle |
| <b>Raise on click</b> | <b>Mesa al primièr plan per un clic</b> | <b>Mesa au purmèr plan per un clic</b> | au \| premier |
| <b>Raise on focus</b> | <b>Metre las fenèstras focalizadas al primièr plan</b> | Conservé : Flexion nouvelle non attestée dans les sources consultées. | au \| mettre \| premier |
| <b>Title _alignment</b> | <b>A_linhament del títol</b> | <b>A_linhament deu títol</b> | du |
| <b>Title fon_t</b> | <b>_Poliça del títol</b> | <b>_Polissa deu títol</b> | du \| police |
| <b>Wrap workspaces when reaching the screen edge</b> | <b>Cambiar d'espaci de trabalh quand lo puntador arriba al bòrd de l'ecran</b> | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | au \| travail |
| Always _Below Other Windows | Totjorn _jos las autras fenèstras | Conservé : Flexion nouvelle non attestée dans les sources consultées. | autre |
| Always on _Visible Workspace | Totjorn _visible suls espacis de trabalh | Totjorn _visible suus espacis de tribalh | sur_les \| travail |
| At the c_enter of the screen | Al _centre de l'ecran | Au _centre de l'ecran | au |
| Automatically _raise windows when they receive focus | Metre las fenèstras al _primièr plan quand son focalizadas | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | au \| mettre \| premier |
| Automatically _tile windows when moving toward the screen edge | Arrengar las _fenèstras de còsta al moment d'un desplaçament cap al bòrd de l'ecran | Conservé : Flexion nouvelle non attestée dans les sources consultées. | au |
| Automatically give focus to _newly created windows | Focalizar automaticament las _novèlas fenèstras | Conservé : Flexion nouvelle non attestée dans les sources consultées. | nouvelle |
| By default, place windows: | Per defaut, plaçar la fenèstra : | Per defaut, plaçar la frinèsta : | fenetre |
| Cannot spawn helper-dialog: %s<br> | Impossible d'aviar la fenèstra d'ajuda : %s<br> | Impossible d'aviar la frinèsta d'ajuda : %s<br> | fenetre |
| Click and drag the buttons to change the layout | Far lisar los botons per modificar lor agençament | Har lisar los botons per modificar lor agençament | faire |
| Close | Tampar | Barrar | fermer |
| Could not create the settings dialog. | Impossible de crear la bóstia de dialòg dels paramètres. | Impossible de crear la bóstia de dialòg deus paramètres. | des |
| Cycle _through windows on all workspaces | Navigar demest las fenèstras de _totes los espacis de trabalh | Conservé : Flexion nouvelle non attestée dans les sources consultées. | tous \| travail |
| Cycle through windows in a _list | Navigar demest las fenèstras dins una _lista | Conservé : Flexion nouvelle non attestée dans les sources consultées. | dans \| une |
| Define shortcuts to perform _window manager actions: | Definir d'acorchis per efectuar d'accions del gestionari de fenèstras : | Conservé : Flexion nouvelle non attestée dans les sources consultées. | du |
| Delay _before raising focused window: | Relambi a_bans la mesa al primièr plan : | Relambi a_bans la mesa au purmèr plan : | au \| premier |
| Do _nothing | _Far pas res | _Har pas res | faire |
| Error reading data from child process: %s<br> | Error al moment de la lectura de las donadas del processus filh : %s<br> | Error au moment de la lectura de las dadas deu processus filh : %s<br> | au \| donnees \| du |
| Fill window | Espandir la fenèstra | Espandir la frinèsta | fenetre |
| Focus follows _mouse | La f_ocalizacion seguís la mirga | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | souris |
| Hide window | Redusir la fenèstra | Redusir la frinèsta | fenetre |
| Keep urgent windows _blinking repeatedly | Far cluquetejar las fenèstras _urgentas fins a la focalizacion | Conservé : Flexion nouvelle non attestée dans les sources consultées. | faire |
| Leave _Fullscreen | Sortir del mòde _ecran complet | Sortir deu mòde _ecran complet | du |
| Margins are areas on the edges of the screen where no window will be placed | Los marges son de zònas al bòrd de l'ecran ont cap de fenèstra serà pas plaçada | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | au \| fenetre |
| Maximize window | Maximizar la fenèstra | Maximizar la frinèsta | fenetre |
| Minimize _Other Windows | Redusir totas las _autras fenèstras | Conservé : Flexion nouvelle non attestée dans les sources consultées. | autre |
| Move to Another Monitor | Desplaçar cap a un autre ecran | Desplaçar cap a un aute ecran | autre |
| Move to Another _Workspace | Desplaçar cap a un autre espaci de _trabalh | Desplaçar cap a un aute espaci de _tribalh | autre \| travail |
| Notify of _urgency by making window's decoration blink | Senhalar una _urgéncia en fasent cluquetejar la decoracion de la fenèstra | Conservé : Sens, accord ou terminologie technique de la source non validés. | fenetre \| une |
| Raise window when clicking _inside application window | Metre una fenèstra al primièr plan en cl_icant a l'interior | Méter ua frinèsta au purmèr plan en cl_icant a l'interior | au \| fenetre \| mettre \| premier \| une |
| Replace the existing window manager | Remplaçar lo gestionari de fenèstra actual | Remplaçar lo gestionari de frinèsta actuau | actuel \| fenetre |
| Reset to Defaults | Reïnicializar a las valors per defaut | Tornar inicializar a las valors per defaut | reinitialiser |
| Restart | Reamodar | Tornar aviar | redemarrer |
| Right | Alinhat a drecha | Alinhat a dreta | droite |
| Roll Window Down | Desenrotlar la fenèstra | Desenrotlar la frinèsta | fenetre |
| Roll Window Up | Enrotlar la fenèstra | Enrotlar la frinèsta | fenetre |
| S_kip windows that have "skip pager"<br>or "skip taskbar" properties set | _Ignorar las fenèstras absentas de la barra dels prètzfaches<br> o de las proprietats « skip pager » e « skip taskbar » | Conservé : Flexion nouvelle non attestée dans les sources consultées. | des |
| Session manager socket | Socket del gestionari de sesilhas | Socket deu gestionari de sessions | du \| session_pluriel |
| Set the compositor mode | Aplicar lo mòde del composidor | Aplicar lo mòde deu composidor | du |
| Settings manager socket | Socket del gestionari de paramètres | Socket deu gestionari de paramètres | du |
| Shade window | Enrotlar la fenèstra | Enrotlar la frinèsta | fenetre |
| Show windows preview in place of icons when cycling | Afichar una previsualizacion de las fenèstras a la plaça de las icònas al moment de la navigacion | Conservé : Flexion nouvelle non attestée dans les sources consultées. | au \| une |
| Stick | Fenèstra peganta (visibla sus totes los espacis de trabalh) | Frinèsta peganta (visibla sus tots los espacis de tribalh) | fenetre \| tous \| travail |
| Switch to win_dow's workspace | Bascuolar dins l'espaci _de trabalh de la fenèstra | Bascuolar dens l'espaci _de tribalh de la frinèsta | dans \| fenetre \| travail |
| The action to perform when the title-bar is double-clicked | Accion d'efectuar al moment d'un clic doble sus la barra de títol | Accion d'efectuar au moment d'un clic doble sus la barra de títol | au |
| The window title cannot be removed | Lo títol de la fenèstra pòt pas èsser suprimit | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | fenetre |
| This will reset all shortcuts to their default values. Do you really want to do this? | Sètz segur que volètz reïnicializar totes los acorchis a lor valor per defaut ? | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | reinitialiser \| tous |
| This window might be busy and is not responding.<br>Do you want to terminate the application? | Aquesta fenèstra respond pas : es possible que siá ocupada.<br>Volètz tampar l'aplicacion ? | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | fenetre \| fermer |
| To other _windows | Per las autras fenèstras | Conservé : Flexion nouvelle non attestée dans les sources consultées. | autre |
| U_nder the mouse pointer | Jol _puntador de la mirga | Jol _puntador de la soritz | souris |
| Use _edge resistance instead of window snapping | _Utilizar la resisténcia als bòrds al luòc de l'aimantacion entre las fenèstras | Conservé : Flexion nouvelle non attestée dans les sources consultées. | au \| aux |
| Use mouse wheel on title bar to ro_ll up the window | Utilizar la rodeta de la mirga sus la barra de títol per enrot_lar la fenèstra | Utilizar la rodeta de la soritz sus la barra de títol per enrot_lar la frinèsta | fenetre \| souris |
| Use the _mouse wheel on the desktop to switch workspaces | Cambiar d'espaci de trabalh en fasent virar la _rodeta de la mirga sul burèu | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | souris \| sur_le \| travail |
| When _moving | Al moment del desplaçament | Au moment deu _desplaçament | au \| du |
| When _resizing | Al moment del redimensionament | Au moment deu _redimensionament | au \| du |
| When a window raises itself: | Quand una fenèstra se plaça al primièr plan : | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | au \| fenetre \| premier \| une |
| With a _dragged window | Amb una fenèstra rebalada | Dab ua frinèsta _rebalada | avec \| une \| fenetre |
| With the mouse _pointer | Amb lo _puntador de la mirga | Dab lo _puntador de la soritz | avec \| souris |
| Workspace %d | Espaci de trabalh %d | Espaci de tribalh %d | travail |
| Workspace Name | Nom de l'espaci de trabalh | Nom de l'espaci de tribalh | travail |
| Workspaces | Espacis de trabalh | Espacis de tribalh | travail |
| Wrap workspaces depending on the actual desktop _layout | Cambiar d'espaci de trabalh en foncion de l'_agençament del burèu | Cambiar d'espaci de tribalh en foncion de l'_agençament deu burèu | du \| travail |
| Wrap workspaces when _the first or the last workspace is reached | Cambiar d'espaci de trabalh quand lo _primièr o lo darrièr es atench | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | derriere \| premier \| travail |
| Zoom desktop with mouse wheel | Agrandir lo burèu amb rodeta de la mirga | Agrandir lo burèu dab rodeta de la soritz | avec \| souris |
| _Bring window on current workspace | _Plaçar la fenèstra dins l'espaci de trabalh actiu | _Plaçar la frinèsta dens l'espaci de tribalh actiu | dans \| fenetre \| travail |
| _Clear | _Escafar | _Desfaçar | effacer |
| _Close | _Tampar | _Barrar | fermer |
| _Delay before window receives focus: | _Relambi abans focalizacion sus una fenèstra : | _Relambi abans focalizacion sus ua frinèsta : | fenetre \| une |
| _Draw frame around selected window while cycling | _Dessenhar un quadre a l'entorn de la fenèstra mesa en evidéncia al moment de la navigacion | _Dessenhar un quadre a l'entorn de la frinèsta mesa en evidéncia au moment de la navigacion | au \| fenetre |
| _Edge resistance: | _Resisténcia als bòrds : | _Resisténcia aus bòrds : | aux |
| _General | _General | _Generau | general |
| _Keyboard | _Clavièr | _Clavèr | clavier |
| _Number of workspaces: | _Nombre d'espacis de trabalh : | _Nombre d'espacis de tribalh : | travail |
| _Raise windows when any mouse button is pressed | _Metre las fenèstras al primièr plan al moment d'un clic mirga | Conservé : Flexion nouvelle non attestée dans les sources consultées. | au \| mettre \| premier \| souris |
| _Remember and recall previous workspace<br>when switching via keyboard shortcuts | _Memorizar l'espaci de trabalh precedent e i tornar<br>al moment d'un cambiament d'espaci via un acorchi de clavièr | _Memorizar l'espaci de tribalh precedent e i tornar<br>au moment d'un cambiament d'espaci via un acorchi de clavèr | au \| clavier \| travail |
| _Reset to Defaults | _Reïnicializar a las valors per defaut | _Tornar inicializar a las valors per defaut | reinitialiser |
| _Same as Other Windows | Coma las autra_s fenèstras | Conservé : Flexion nouvelle non attestée dans les sources consultées. | autre \| comme |
| _Workspaces | _Espacis de trabalh | _Espacis de tribalh | travail |
| windows;behavior;settings;preferences;cycling;cycle;switching;focus;raises;accessibility;key;dragging;move;moving;hide;frame;title bar;maximized;tile;screen;edge;hot corner;snapping;mouse wheel;roll up;workspaces;placement;compositor;compositing;enable;disable;shadows;decorations;opacity;resize;inactive;preview;compiz;transitions; | windows;behavior;settings;preferences;cycling;cycle;switching;focus;raises;accessibility;key;dragging;move;moving;hide;frame;title bar;maximized;tile;screen;edge;hot corner;snapping;mouse wheel;roll up;workspaces;placement;compositor;compositing;enable;disable;shadows;decorations;opacity;resize;inactive;preview;compiz;transitions;apercebut;transicions;opacitat;talha;ombra;plaçament;espaci;trabalh;ecran;conh;cunh;mirga;barra;titol;comportament;preferéncias;bascular;clau;accessibilitat;paramètres;fenèstra;finèstra; | Conservé : Contexte technique ou long : relecture intégrale nécessaire. | fenetre \| souris \| travail |
| windows;management;settings;preferences;themes;styles;decorations;title bar;font;buttons;menu;minimize;maximize;shade;roll up;layout;keyboard shortcuts;focus;snapping;screen;workspaces;edges;corner;hide content;move;resize;moving;resizing;double click; | windows;management;settings;preferences;themes;styles;decorations;title bar;font;buttons;menu;minimize;maximize;shade;roll up;layout;keyboard shortcuts;focus;snapping;screen;workspaces;edges;corner;hide content;move;resize;moving;resizing;double click;fenèstra;gestion;paramètres;reglatges;preferéncias;tèmas;estil;titol;barra;poliça;boton;menú;clavièr;ecran;amagar;rescondre;esconder;acorchis;conh;cunh; | Conservé : Contexte technique ou long : relecture intégrale nécessaire. | clavier \| fenetre \| police |
| workspaces;settings;preferences;virtual desktops;number;windows;screen;margins; | workspaces;settings;preferences;virtual desktops;number;windows;screen;margins;espaci;trabalh;paramètres;preferéncias;burèu;nombre;fenèstra;finèstra;ecran; | workspaces;settings;preferences;virtual desktops;number;windows;screen;margins;espaci;tribalh;paramètres;preferéncias;burèu;nombre;frinèsta;finèstra;ecran; | fenetre \| travail |

## tuxpaint

| Clé source | Occitan livré | Béarnais retenu ou motif de conservation | Glossaire |
|---|---|---|---|
| A drawing program for children. | Un logicial de dessenh pels mainatges. | Un logiciau de dessenh entaus mainatges. | logiciel \| dessin \| pour_les \| enfant |
| A square is a rectangle with four equal sides. | Un carrat es un rectangle amb quatre costats egals. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | avec |
| Blue! | Blau ! | Blu ! | bleu |
| Bye bye! | Al còp que ven ! | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | au |
| Drawing program | Logicial de dessenh | Logiciau de dessenh | logiciel |
| Eraser | Goma | Gòma | gomme |
| Eraser! | Goma ! | Desfaçar ! | effacer |
| Fill | Emplenar | Plear | remplir |
| Fills | Emplenar | Plear | remplir |
| Good job! | Bon trabalh ! | Bon tribalh ! | travail |
| Keep it up! | Contunha aital ! | Contunhar ! | continuer |
| New | Nòu | Navèth | nouveau |
| No, don’t bother saving! | Non, te copes pas lo cap per enregistrar ! | Non, quitar shens enregistrar ! | non \| quitter \| sans \| enregistrer |
| No, don’t erase it! | Non, lo gomes pas ! | Non, anullar ! | non \| annuler |
| No, take me back! | Non, fai pas tornar ! | Non, tornar ! | non \| retour |
| Open | Dubrir | Obrir | ouvrir |
| Open… | Dubrir… | Obrir… | ouvrir |
| Please wait… | Esperatz… | Esperar… | attendre |
| Print your picture now? | Imprimir aqueste imatge ara ? | Imprimir l'imatge ara ? | imprimer \| image \| maintenant |
| Purple! | Violet ! | Vriulet ! | violet |
| Quit | Sortir | Quitar | quitter |
| Red! | Roge ! | Roi ! | rouge |
| Redo | Tornar far | Tornar har | refaire |
| Redo! | Tornar far ! | Tornar har ! | refaire |
| Sky blue! | Blau cèl ! | Blu cèu ! | bleu |
| Text | Tèxt | Tèxte | texte |
| There are no saved files! | I a pas de fichièr enregistrat ! | Nat fichèr enregistrat ! | aucun \| fichier |
| Tools | Espleches | Utís | outil |
| Yes, I’m done! | Òc, ai acabat ! | Òc, quitar ! | oui \| quitter |
| Yes, erase it! | Òc, goma-lo ! | Òc, suprimir ! | oui \| supprimer |
| Yes, print it! | Òc, imprimís-lo ! | Òc, imprimir ! | oui \| imprimer |
| Yes, save it! | Òc, enregistra-la ! | Òc, enregistrar ! | oui \| enregistrer |
| You can’t print yet! | Lo podètz pas encara imprimir ! | Impossible d'imprimir enqüèra ! | impossible \| imprimer \| encore |

## lightdm

| Clé source | Occitan livré | Béarnais retenu ou motif de conservation | Glossaire |
|---|---|---|---|
| Catalogue vide | | Aucun remplacement | |

## ristretto

| Clé source | Occitan livré | Béarnais retenu ou motif de conservation | Glossaire |
|---|---|---|---|
| %s: %s<br><br>Try %s --help to see a full list of<br>available command line options.<br> | %s : %s<br><br>%s --help per veire una lista completa<br>de las opcions en linha de comanda.<br> | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | une \| voir |
| Active item text color | Activar la color del tèxte de l'element | Color deu tèxte de l'element actiu | couleur \| du \| texte \| element \| actif |
| All Files | Totes los fichièrs | Tots los fichèrs | fichier \| tous |
| Are you sure you want to delete image '%s' from disk? | Sètz segur que volètz suprimir l'imatge « %s » del disc ? | Suprimir l'imatge « %s » deu disc ? | supprimer \| image \| du \| disque |
| Are you sure you want to send image '%s' to trash? | Sètz segur que volètz metre l'imatge « %s » dins l'escobilhièr ? | Méter l'imatge « %s » dens l'escobilhièr ? | mettre \| image \| dans |
| Choose 'set wallpaper' method | Causir lo metòde per 'Utilizar en tant que fons d'ecran ' | Causir lo metòde per 'Utilizar en tant que hons d'ecran ' | fond |
| Clear private data | Escafar las donadas personalas | Desfaçar las dadas personaus | donnees \| effacer \| personnel |
| Close this image | Tampar aqueste imatge | Barrar l'imatge | fermer \| image |
| Configure which system is currently managing your desktop.<br>This setting determines the method <i>Ristretto</i> will use<br>to configure the desktop wallpaper. | Indicar quin sistèma gerís vòstre burèu actualment.<br>Aqueste reglatge permetrà a <i>Ristretto</i> de determinar lo metòde<br>adeqüat per cambiar lo fons d'ecran . | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | fond |
| Could not save file | Impossible de salvar lo fichièr | Impossible de enregistrar lo fichèr | enregistrer \| fichier |
| Cursor item text color | Color del tèxte de l'element del cursor | Color deu tèxte de l'element deu cursor | du |
| Delete this image from disk | Suprimir aqueste imatge del disc | Suprimir l'imatge deu disc | supprimer \| image \| du \| disque |
| Display ristretto user manual | Afichar lo manual de ristretto | Afichar lo manuau de ristretto | manuel |
| Do _not show this message again | Afichar pas mai aqueste _messatge | Non pas tornar afichar aqueth _messatge | non \| retour \| afficher \| message |
| Edit this image | Editar aqueste imatge | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | modifier |
| Edit with | Editar amb | Modificar dab | avec \| modifier |
| Empty | Void | Vueit | vide |
| F_irst | Pri_mièr | Pur_mèr | premier |
| First image | Primièr imatge | Purmèr imatge | premier |
| General | General | Generau | general |
| Icon Bar Model | Modèl de barra d'icòna | Modèle de barra d'icòna | modele |
| Image Viewer Preferences | Preferéncias del visionador d’imatges | Preferéncias deu visionador d’imatges | du |
| Invert zoom direction | Inversar la direccion del zoom | Inversar la direccion deu zoom | du |
| Large | Grand | Gran | grand |
| Larger | Mai grand | Mei gran | grand \| plus |
| Last Four Hours | Las quatre darrièras oras | Las quate darrèras òras | derniere \| heure |
| Last Hour | La darrièra ora | La darrèra òra | derniere \| heure |
| Last Two Hours | Los doas darrièras oras | Las duas darrèras òras | derniere \| heure |
| Last image | Darrièr imatge | Darrèr imatge | derriere |
| Limit rendering quality | Limitar la qualitat del rendut | Limitar la qualitat deu rendut | du |
| Maximize window on startup when opening an image | Maximizar la fenèstra a la dobertura d'un imatge | Maximizar la frinèsta a la obertura d'un imatge | fenetre \| ouvrir |
| Model for the icon bar | Modèl per la barra d'icònas | Modèle per la barra d'icònas | modele |
| Normal | _Talha Normala | Talha normau | taille \| normal |
| Open %s and other files of type %s with: | Dobrir %s e los autres fichièrs del tipe %s amb : | Obrir %s e los autes fichèrs deu tipe %s dab : | autres \| avec \| du \| fichier \| ouvrir |
| Open With Other _Application... | Dobrir amb una autra _aplicacion... | Obrir dab ua auta _aplicacion... | autre \| avec \| ouvrir \| une |
| Open an image | Dobrir un imatge | Obrir un imatge | ouvrir |
| Open image | Dobrir un imatge | Obrir un imatge | ouvrir |
| Other Applications | Autras aplicacions | Autas aplicacions | autre |
| Pause slideshow | Metre lo diaporama en pausa | Méter lo diaporama en pausa | mettre |
| Press open to select an image | Quichatz sus Dobrir per seleccionar un imatge | Obrir entà seleccionar un imatge | ouvrir \| pour \| selectionner \| image |
| Right | Drecha | Dreta | droite |
| Rotate _Right | Rotacion cap a _drecha | Rotacion cap a _dreta | droite |
| Save a copy of the image | Enregistrar una còpia de l'imatge | Enregistrar ua còpia de l'imatge | une |
| Save copy | Salvar una còpia | Enregistrar ua còpia | enregistrer \| une |
| Scroll wheel | Rodeta de la mirga | Rodeta de la soritz | souris |
| Set as _Wallpaper... | _Utilizar coma fons d'ecran ... | _Utilizar com hons d'ecran ... | comme \| fond |
| Set as wallpaper | Utilizar coma fons d'ecran  | Utilizar com hons d'ecran  | comme \| fond |
| Show an analog clock that displays the current time when the window is fullscreen | Afichar un relòtge analogic qu'afiche l'ora correnta quand la fenèstra es en ecran complet  | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | fenetre \| heure |
| Show file properties | Afichar las proprietats del fichièr | Afichar las proprietats deu fichèr | du \| fichier |
| Show settings dialog | Afichar la fenèstra de las preferéncias | Afichar la frinèsta de las preferéncias | fenetre |
| Small | Pichon | Petit | petit |
| Smaller | Mai pichon | Mei petit | petit \| plus |
| The thumbnailer-service can not be reached,<br>for this reason, the thumbnails can not be<br>created.<br><br>Install <b>Tumbler</b> or another <i>thumbnailing daemon</i><br>to resolve this issue. | Impossible d'aviar lo servici de las miniaturas.<br>Las miniaturas pòdon doncas pas èsser<br>creadas.<br><br>Installatz <b>Tumbler</b> o un autre <i>demòni de creacion<br>de miniaturas</i> per resòlvre aqueste problèma. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | autre |
| Time range to clear: | Periòde de temps a escafar :  | Periòde de temps a desfaçar :  | effacer |
| Today | Uèi | Uei | aujourdhui |
| Top | Naut | Haut | haut |
| Use as _default for this kind of file | Utilizar per _defaut per aqueste tipe de fichièr | Utilizar per _defaut entà aqueth tipe de fichèr | utiliser \| pour \| type \| fichier |
| Very Large | Fòrt grand | Hòrt gran | grand \| tres |
| Very Small | Fòrt pichon | Hòrt petit | petit \| tres |
| Wrap around images | Enrodar a l'entorn dels imatges | Enrodar a l'entorn deus imatges | des |
| Zoom _Fit | Zoom al _melhor | Zoom au _melhor | au |
| Zoom to fit window | Zoomer per ajustar a la fenèstra | Zoomer per ajustar a la frinèsta | fenetre |
| _Clear private data... | _Netejar las donadas personalas... | _Netejar las dadas personaus... | donnees \| personnel |
| _Close | _Tampar | _Barrar | fermer |
| _Contents | _Contengut | _Contiengut | contenu |
| _Delete | _Escafar | _Desfaçar | effacer |
| _Edit | _Editar | _Modificar | modifier |
| _File | _Fichièr | _Fichèr | fichier |
| _Last | _Darrièr | _Darrèr | derriere |
| _Normal Size | _Talha normala | _Talha normau | normal |
| _Open | _Dobrir | _Obrir | ouvrir |
| _Open with | _Dobrir amb | _Obrir dab | avec \| ouvrir |
| _Open... | _Dobrir... | _Obrir... | ouvrir |
| _Save copy... | _Enregistrar una còpia... | _Enregistrar ua còpia... | une |

## xfce4-pulseaudio-plugin

| Clé source | Occitan livré | Béarnais retenu ou motif de conservation | Glossaire |
|---|---|---|---|
| Adjust the audio volume of the PulseAudio sound system | Ajustar lo volum del sistèma àudio PulseAudio | Ajustar lo volum deu sistèma àudio PulseAudio | du |
| All | Totes | Tots | tous |
| Audio mixer command that can be executed from the context menu, e.g. "pavucontrol", "unity-control-center sound". | Comanda del mixador àudio d'executar dempuèi lo menú contextual, p. ex. « pavucontrol » o « unity-control-center sound ». | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | du |
| Clear Known Items | Escafar los elements coneguts | Desfaçar los elements coneguts | effacer |
| Enable keyboard _shortcuts for volume control | Activar los acorchi_s de clavièr pel contraròtle del volum | Activar los acorchi_s de clavèr entau contraròtle deu volum | clavier \| du \| pour_le |
| Enables volume control using multimedia keys. Make sure no other application that listens to these keys (e.g. xfce4-volumed) is running in the background. | Activa lo contraròtle del volum amb las tòcas multimèdia. Asseguratz-vos que cap d'autra aplicacion qu'escota aquelas tòcas (p. ex. xfce4-volumed) vire en rèireplan. | Conservé : Phrase conjuguée, adresse personnelle ou phrase complète à valider. | autre \| avec \| du |
| General | General | Generau | general |
| Not connected to the PulseAudio server | Pas connectat al servidor PulseAudio | Pas connectat au servidor PulseAudio | au |
| PulseAudio Panel Plugin | Empeuton del tablèu de bòrd PulseAudio | Empeuton deu panèu PulseAudio | du \| panneau |

## lightdm-gtk-greeter

| Clé source | Occitan livré | Béarnais retenu ou motif de conservation | Glossaire |
|---|---|---|---|
| Are you sure you want to close all programs and restart the computer? | Volètz vertadièrament quitar totes los programas e reaviar l’ordenador ? | Barrar tots los programas e tornar aviar l'ordinator ? | fermer \| tous \| programme \| redemarrer \| ordinateur |
| Are you sure you want to close all programs and shut down the computer? | Volètz vertadièrament quitar totes los programas e atudar l’ordenador ? | Barrar tots los programas e estupar l'ordinator ? | fermer \| tous \| programme \| eteindre \| ordinateur |
| Enter your password | Picatz vòstre senhal | Picar lo mot de passa | saisir \| mot_de_passe |
| Enter your username | Picatz vòstre nom d’utilizaire | Picar lo nom d'utilizator | saisir \| nom \| utilisateur |
| Failed to authenticate | Fracàs de l'autentificacion | Error d'autentificacion | erreur |
| Failed to start session | La session a pas pogut s'aviar | Impossible d'aviar la session | impossible \| lancer \| session |
| Large Text | Grand tèxte | Gran tèxte | grand |
| Log In | Connexion | Obrir la session | ouvrir \| session |
| OK | D'acòrdi | D'acòrd | accord |
| On Screen Keyboard | Clavièr visual | Clavèr visual | clavier |
| Other | Autre | Aute | autre |
| Other... | Autre... | Aute... | autre |
| Restart | Reaviar | Tornar aviar | redemarrer |
| Restart... | Reaviar... | Tornar aviar... | redemarrer |
| Shut Down | Atudar | Estupar | eteindre |
| Shut Down... | Atudar... | Estupar... | eteindre |
| Suspend | Metre en velha | Méter en velha | mettre |
| Unlock | Desverrolhar | Desvarrolhar | deverrouiller |
| Warning: There is still %d user logged in. | Atencion : i a encara %d utilizaire connectat. / Atencion : i a encara %d utilizaires connectats. | Conservé : Pluriel gettext : validation de toutes les formes requise. |  |
