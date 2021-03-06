<?php

require "Composer.php";

/**
 * Description of ComposerData
 *
 * @author nbuser
 */
class ComposerData {

    public $composers;

    function __construct() {
        $this->composers = array(
            new Composer("1", "Johann Sebastian", "Bach", "Baroque"),
            new Composer("2", "Arcangelo", "Corelli", "Baroque"),
            new Composer("3", "George Frideric", "Handel", "Baroque"),
            new Composer("4", "Henry", "Purcell", "Baroque"),
            new Composer("5", "Jean-Philippe", "Rameau", "Baroque"),
            new Composer("6", "Domenico", "Scarlatti", "Baroque"),
            new Composer("7", "Antonio", "Vivaldi", "Baroque"),
            new Composer("8", "Ludwig van", "Beethoven", "Classical"),
            new Composer("9", "Johannes", "Brahms", "Classical"),
            new Composer("10", "Francesco", "Cavalli", "Classical"),
            new Composer("11", "Fryderyk Franciszek", "Chopin", "Classical"),
            new Composer("12", "Antonin", "Dvorak", "Classical"),
            new Composer("13", "Franz Joseph", "Haydn", "Classical"),
            new Composer("14", "Gustav", "Mahler", "Classical"),
            new Composer("15", "Wolfgang Amadeus", "Mozart", "Classical"),
            new Composer("16", "Johann", "Pachelbel", "Classical"),
            new Composer("17", "Gioachino", "Rossini", "Classical"),
            new Composer("18", "Dmitry", "Shostakovich", "Classical"),
            new Composer("19", "Richard", "Wagner", "Classical"),
            new Composer("20", "Louis-Hector", "Berlioz", "Romantic"),
            new Composer("21", "Georges", "Bizet", "Romantic"),
            new Composer("22", "Cesar", "Cui", "Romantic"),
            new Composer("23", "Claude", "Debussy", "Romantic"),
            new Composer("24", "Edward", "Elgar", "Romantic"),
            new Composer("25", "Gabriel", "Faure", "Romantic"),
            new Composer("26", "Cesar", "Franck", "Romantic"),
            new Composer("27", "Edvard", "Grieg", "Romantic"),
            new Composer("28", "Nikolay", "Rimsky-Korsakov", "Romantic"),
            new Composer("29", "Franz Joseph", "Liszt", "Romantic"),
            new Composer("30", "Felix", "Mendelssohn", "Romantic"),
            new Composer("31", "Giacomo", "Puccini", "Romantic"),
            new Composer("32", "Sergei", "Rachmaninoff", "Romantic"),
            new Composer("33", "Camille", "Saint-Saens", "Romantic"),
            new Composer("34", "Franz", "Schubert", "Romantic"),
            new Composer("35", "Robert", "Schumann", "Romantic"),
            new Composer("36", "Jean", "Sibelius", "Romantic"),
            new Composer("37", "Bedrich", "Smetana", "Romantic"),
            new Composer("38", "Richard", "Strauss", "Romantic"),
            new Composer("39", "Pyotr Il'yich", "Tchaikovsky", "Romantic"),
            new Composer("40", "Guiseppe", "Verdi", "Romantic"),
            new Composer("41", "Bela", "Bartok", "Post-Romantic"),
            new Composer("42", "Leonard", "Bernstein", "Post-Romantic"),
            new Composer("43", "Benjamin", "Britten", "Post-Romantic"),
            new Composer("44", "John", "Cage", "Post-Romantic"),
            new Composer("45", "Aaron", "Copland", "Post-Romantic"),
            new Composer("46", "George", "Gershwin", "Post-Romantic"),
            new Composer("47", "Sergey", "Prokofiev", "Post-Romantic"),
            new Composer("48", "Maurice", "Ravel", "Post-Romantic"),
            new Composer("49", "Igor", "Stravinsky", "Post-Romantic"),
            new Composer("50", "Carl", "Orff", "Post-Romantic"),
        );
    }

}
?>