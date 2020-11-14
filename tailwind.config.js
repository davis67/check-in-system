module.exports = {
    future: {
        // removeDeprecatedGapUtilities: true,
        // purgeLayersByDefault: true,
    },
    purge: [],
    theme: {
        extend: {
            fontFamily: {
                sans: ['Roboto']
            },
            minHeight: {
                "50vh": "50vh",
                "75vh": "75vh"
            }
        },
    },
    variants: {},
    plugins: [require('@tailwindcss/ui')],
}